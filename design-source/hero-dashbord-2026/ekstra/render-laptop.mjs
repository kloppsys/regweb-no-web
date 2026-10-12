import {createRequire} from 'module';
const require=createRequire('/Users/boss/.cache/sjekk-mobiloverflyt/package.json');
const p=require('puppeteer-core');
const b=await p.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',args:['--allow-file-access-from-files']});
const pg=await b.newPage();await pg.setViewport({width:1760,height:960});
await pg.goto('file://'+process.argv[2]);await new Promise(r=>setTimeout(r,500));
const h=await pg.evaluate(()=>document.querySelector('.wrap').getBoundingClientRect().height);
await pg.screenshot({path:process.argv[3],omitBackground:true,clip:{x:0,y:0,width:1760,height:Math.ceil(h)}});console.log(h);await b.close();
