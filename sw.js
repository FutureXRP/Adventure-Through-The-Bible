/* Footsteps service worker — installability + offline reading.
 * Docs are network-first (so deploys show up immediately); static assets are
 * cache-first (fast, and available offline). Supabase API calls are never
 * intercepted, so auth and data stay live. Bump CACHE to force a refresh. */
const CACHE = 'footsteps-v1';
const CORE = [
  './', './index.html', './account.html', './login.html', './admin.html',
  './stories.json', './stories-tier2.json', './prologue.json',
  './manifest.webmanifest',
  './icons/icon-192.png', './icons/icon-512.png', './icons/icon-180.png'
];

self.addEventListener('install', e => {
  e.waitUntil((async () => {
    const c = await caches.open(CACHE);
    await Promise.allSettled(CORE.map(u => c.add(u)));
    await self.skipWaiting();
  })());
});

self.addEventListener('activate', e => {
  e.waitUntil((async () => {
    const keys = await caches.keys();
    await Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)));
    await self.clients.claim();
  })());
});

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  const sameOrigin = url.origin === location.origin;
  const cacheable = sameOrigin
    || url.hostname === 'fonts.googleapis.com'
    || url.hostname === 'fonts.gstatic.com'
    || url.hostname === 'cdn.jsdelivr.net';
  if (!cacheable) return; // Supabase API and everything else: straight to network

  const isDoc = req.mode === 'navigate'
    || (sameOrigin && (url.pathname.endsWith('.html') || url.pathname.endsWith('.json')));

  if (isDoc) {
    e.respondWith((async () => {
      try {
        const r = await fetch(req);
        const c = await caches.open(CACHE); c.put(req, r.clone());
        return r;
      } catch (err) {
        const cached = await caches.match(req);
        return cached || (req.mode === 'navigate'
          ? caches.match('./index.html')
          : new Response('', { status: 503, statusText: 'Offline' }));
      }
    })());
  } else {
    e.respondWith((async () => {
      const cached = await caches.match(req);
      if (cached) return cached;
      const r = await fetch(req);
      if (r && r.ok) { const c = await caches.open(CACHE); c.put(req, r.clone()); }
      return r;
    })());
  }
});
