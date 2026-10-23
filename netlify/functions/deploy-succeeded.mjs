// Runs after every successful Netlify deploy. On production deploys it sends every URL
// in the sitemap to IndexNow (Bing, Yandex, Seznam, Naver and others share the ping).
const HOST = 'polarisglobal.io';
const KEY = 'd225142c66ac2deb313c58cfabb8f555';

const locs = (xml) => [...xml.matchAll(/<loc>([^<]+)<\/loc>/g)].map((m) => m[1]);

export const handler = async (event) => {
  let deploy = {};
  try { deploy = JSON.parse(event.body || '{}').payload || {}; } catch {}
  if (deploy.context && deploy.context !== 'production') return { statusCode: 200, body: 'skipped: not production' };
  try {
    const index = await (await fetch(`https://${HOST}/sitemap-index.xml`)).text();
    let urlList = [];
    for (const sm of locs(index)) urlList = urlList.concat(locs(await (await fetch(sm)).text()));
    const res = await fetch('https://api.indexnow.org/indexnow', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json; charset=utf-8' },
      body: JSON.stringify({ host: HOST, key: KEY, keyLocation: `https://${HOST}/${KEY}.txt`, urlList }),
    });
    console.log(`IndexNow: ${res.status} for ${urlList.length} URLs`);
    return { statusCode: 200, body: `IndexNow ${res.status}` };
  } catch (e) {
    console.log(`IndexNow failed: ${e.message}`);
    return { statusCode: 200, body: 'IndexNow failed' };
  }
};
