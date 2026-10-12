// Renders hero.html to PNG (2336x1314). Usage: node render.mjs [out.png]
// Needs puppeteer-core (e.g. ~/.cache/sjekk-mobiloverflyt) and Google Chrome.
import {createRequire} from 'module';
import {fileURLToPath} from 'url';
import path from 'path';
const require=createRequire('/Users/boss/.cache/sjekk-mobiloverflyt/package.json');
const p=require('puppeteer-core');
const dir=path.dirname(fileURLToPath(import.meta.url));
const out=process.argv[2]||path.join(dir,'hero-ny.png');
const b=await p.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',args:['--allow-file-access-from-files']});
const pg=await b.newPage();await pg.setViewport({width:2336,height:1314,deviceScaleFactor:1});
await pg.goto('file://'+path.join(dir,'hero.html'));await pg.evaluate(()=>document.fonts.ready);
await pg.screenshot({path:out});await b.close();console.log(out);
