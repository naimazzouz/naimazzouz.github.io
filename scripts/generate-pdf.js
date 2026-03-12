#!/usr/bin/env -S NODE_PATH=/opt/node22/lib/node_modules node
/**
 * generate-pdf.js — Génération de PDF imprimables depuis les pages du site
 *
 * Usage :
 *   node scripts/generate-pdf.js <chemin-html> [--output <fichier.pdf>] [--no-corrections]
 *
 * Exemples :
 *   node scripts/generate-pdf.js maths/seconde/ch01/lecon.html
 *   node scripts/generate-pdf.js maths/seconde/ch01/exercices.html --no-corrections
 *   node scripts/generate-pdf.js maths/seconde/ch01/lecon.html --output mon-cours.pdf
 *
 * Dépendances : playwright (npm install -g playwright)
 */

const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const http = require('http');

// ── Lecture des arguments ──
const args = process.argv.slice(2);

if (args.length === 0 || args.includes('--help') || args.includes('-h')) {
  console.log(`
╔══════════════════════════════════════════════════════╗
║       Générateur de PDF — Maths & Sciences LP        ║
╚══════════════════════════════════════════════════════╝

Usage :
  node scripts/generate-pdf.js <chemin-html> [options]

Options :
  --output, -o <fichier>   Nom du fichier PDF de sortie
  --no-corrections         Masquer les corrections dans le PDF
  --help, -h               Afficher cette aide

Exemples :
  node scripts/generate-pdf.js maths/seconde/ch01/lecon.html
  node scripts/generate-pdf.js maths/seconde/ch01/exercices.html --no-corrections -o exercices-ch01.pdf
`);
  process.exit(0);
}

const htmlPath = args[0];
let outputPath = null;
let showCorrections = true;

for (let i = 1; i < args.length; i++) {
  if ((args[i] === '--output' || args[i] === '-o') && args[i + 1]) {
    outputPath = args[++i];
  } else if (args[i] === '--no-corrections') {
    showCorrections = false;
  }
}

// ── Vérification du fichier source ──
const rootDir = path.resolve(__dirname, '..');
const absoluteHtmlPath = path.resolve(rootDir, htmlPath);

if (!fs.existsSync(absoluteHtmlPath)) {
  console.error(`Erreur : fichier introuvable — ${absoluteHtmlPath}`);
  process.exit(1);
}

// ── Nom de sortie par défaut ──
if (!outputPath) {
  const parts = htmlPath.replace(/\.html$/, '').split('/').filter(Boolean);
  const pdfDir = path.join(rootDir, 'pdf', 'generated');
  if (!fs.existsSync(pdfDir)) fs.mkdirSync(pdfDir, { recursive: true });
  outputPath = path.join(pdfDir, parts.join('-') + '.pdf');
}

if (!path.isAbsolute(outputPath)) {
  outputPath = path.resolve(process.cwd(), outputPath);
}

// ── CSS d'impression à injecter ──
const printCssPath = path.join(rootDir, 'print.css');
const printCss = fs.existsSync(printCssPath) ? fs.readFileSync(printCssPath, 'utf8') : '';

// Extraire le contenu du @media print { ... }
const printCssContent = printCss.replace(/@media\s+print\s*\{/, '').replace(/\}\s*$/, '');

// ── Serveur HTTP local ──
function createServer(rootDir) {
  return new Promise((resolve) => {
    const mimeTypes = {
      '.html': 'text/html',
      '.css': 'text/css',
      '.js': 'application/javascript',
      '.json': 'application/json',
      '.png': 'image/png',
      '.jpg': 'image/jpeg',
      '.svg': 'image/svg+xml',
      '.woff2': 'font/woff2',
      '.woff': 'font/woff',
      '.ttf': 'font/ttf',
    };

    const server = http.createServer((req, res) => {
      let filePath = path.join(rootDir, decodeURIComponent(req.url.split('?')[0]));
      if (filePath.endsWith('/')) filePath += 'index.html';

      const ext = path.extname(filePath).toLowerCase();
      const contentType = mimeTypes[ext] || 'application/octet-stream';

      fs.readFile(filePath, (err, data) => {
        if (err) {
          res.writeHead(404);
          res.end('Not found');
          return;
        }
        res.writeHead(200, { 'Content-Type': contentType });
        res.end(data);
      });
    });

    server.listen(0, '127.0.0.1', () => {
      const port = server.address().port;
      resolve({ server, port });
    });
  });
}

// ── Génération du PDF ──
async function generatePDF() {
  console.log('🖨️  Génération du PDF...');
  console.log(`   Source : ${htmlPath}`);
  console.log(`   Sortie : ${outputPath}`);
  if (!showCorrections) console.log('   Mode  : sans corrections');

  // Démarrer le serveur local
  const { server, port } = await createServer(rootDir);
  const relPath = path.relative(rootDir, absoluteHtmlPath);
  const url = `http://127.0.0.1:${port}/${relPath}`;

  console.log(`   URL    : ${url}`);

  let browser;
  try {
    browser = await chromium.launch({
      headless: true,
      args: ['--no-sandbox', '--disable-setuid-sandbox'],
    });

    const page = await browser.newPage();

    // Naviguer vers la page
    await page.goto(url, { waitUntil: 'networkidle', timeout: 60000 });

    // Attendre le rendu MathJax (jusqu'à 15s)
    console.log('   ⏳ Attente du rendu MathJax...');
    try {
      await page.waitForFunction(() => {
        // MathJax v3 : vérifier que le typesetting est terminé
        if (typeof MathJax !== 'undefined' && MathJax.startup) {
          return MathJax.startup.promise !== undefined;
        }
        // Pas de MathJax sur la page — OK
        return true;
      }, { timeout: 15000 });

      // Attendre que MathJax ait fini son travail
      await page.evaluate(() => {
        if (typeof MathJax !== 'undefined' && MathJax.startup && MathJax.startup.promise) {
          return MathJax.startup.promise;
        }
      });
    } catch {
      console.log('   ⚠️  MathJax timeout — poursuite sans attendre');
    }

    // Attendre que Chart.js ait fini de dessiner (petite pause)
    await page.waitForTimeout(2000);

    // Convertir les canvas Chart.js en images statiques
    console.log('   📊 Conversion des graphiques Chart.js...');
    await page.evaluate(() => {
      document.querySelectorAll('canvas').forEach((canvas) => {
        try {
          const dataUrl = canvas.toDataURL('image/png', 1.0);
          const img = document.createElement('img');
          img.src = dataUrl;
          img.style.maxWidth = '100%';
          img.style.height = 'auto';
          img.style.display = 'block';
          img.style.margin = '0 auto';
          canvas.parentNode.replaceChild(img, canvas);
        } catch {
          // Canvas tainted ou non accessible — on le laisse
        }
      });
    });

    // Injecter le CSS d'impression en mode écran (pour le PDF)
    console.log('   🎨 Application du style d\'impression...');
    await page.addStyleTag({ content: printCssContent });

    // Masquer les éléments de navigation injectés par nav.js
    await page.addStyleTag({
      content: `
        .sn-breadcrumb, .sn-ch-menu, .sn-ch-nav, .sn-back-top, .sn-toc,
        .nb, .nav-footer, .nav-bottom, .nav-links, .nav-btn, .nav-link,
        .nav-back, .nav-fwd,
        .bc, .bcq, .btn-corr, .flash-btn,
        .ctrl-vis, .slider-row,
        .anim-wrap button {
          display: none !important;
        }

        body {
          background: #fff;
          padding: 0;
          margin: 0;
        }

        .c, .container {
          max-width: 100%;
          border: none;
          border-radius: 0;
          box-shadow: none;
          padding: 0;
          margin: 0;
        }
      `,
    });

    // Afficher ou masquer les corrections
    if (showCorrections) {
      await page.addStyleTag({
        content: `
          .corr, .correction, .qcm-corr, .flash-corr {
            display: block !important;
          }
        `,
      });
    } else {
      await page.addStyleTag({
        content: `
          .corr, .correction, .qcm-corr, .flash-corr,
          .corr-wrap, .corr-body, .corr-btn {
            display: none !important;
          }
        `,
      });
    }

    // Petite pause pour que les styles soient appliqués
    await page.waitForTimeout(500);

    // Générer le PDF
    console.log('   📄 Export PDF...');
    await page.pdf({
      path: outputPath,
      format: 'A4',
      margin: {
        top: '18mm',
        right: '15mm',
        bottom: '20mm',
        left: '15mm',
      },
      printBackground: true,
      preferCSSPageSize: false,
      displayHeaderFooter: true,
      headerTemplate: `
        <div style="font-size:7pt; color:#999; width:100%; text-align:center; padding:0 15mm;">
          <span style="font-weight:600;">Maths & Sciences LP</span>
        </div>
      `,
      footerTemplate: `
        <div style="font-size:7pt; color:#999; width:100%; display:flex; justify-content:space-between; padding:0 15mm;">
          <span>maths-sciences-lp.github.io</span>
          <span>Page <span class="pageNumber"></span> / <span class="totalPages"></span></span>
        </div>
      `,
    });

    const stats = fs.statSync(outputPath);
    const sizeMB = (stats.size / 1024 / 1024).toFixed(2);
    console.log(`\n✅ PDF généré avec succès !`);
    console.log(`   📁 ${outputPath} (${sizeMB} Mo)`);
  } catch (err) {
    console.error('\n❌ Erreur lors de la génération :', err.message);
    process.exit(1);
  } finally {
    if (browser) await browser.close();
    server.close();
  }
}

generatePDF();
