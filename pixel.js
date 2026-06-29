/* ════════════════════════════════════════════════════════════════
 * Meta (Facebook / Instagram) Pixel for Footsteps
 * ────────────────────────────────────────────────────────────────
 * 1) Create a Pixel in Meta Events Manager (Data Sources → Web).
 * 2) Paste its numeric ID into META_PIXEL_ID below.
 *    Leave it blank to disable tracking entirely (nothing loads, no errors).
 *
 * Events this site fires:
 *   • PageView             — every page, automatically
 *   • CompleteRegistration — on account sign-up (login.html)
 *   • StoryComplete        — custom; first time a signed-in reader finishes a story
 *
 * For ad optimization, optimize toward CompleteRegistration (or Purchase, once
 * you have a checkout). StoryComplete is a strong engagement signal for building
 * "engaged reader" lookalike audiences later.
 * ════════════════════════════════════════════════════════════════ */
window.META_PIXEL_ID = ''; // ← put your Pixel ID here, e.g. '1234567890987654'

(function () {
  var id = window.META_PIXEL_ID;
  if (!id) return; // not configured → nothing loads
  !function (f, b, e, v, n, t, s) {
    if (f.fbq) return; n = f.fbq = function () { n.callMethod ?
      n.callMethod.apply(n, arguments) : n.queue.push(arguments); };
    if (!f._fbq) f._fbq = n; n.push = n; n.loaded = !0; n.version = '2.0';
    n.queue = []; t = b.createElement(e); t.async = !0; t.src = v;
    s = b.getElementsByTagName(e)[0]; s.parentNode.insertBefore(t, s);
  }(window, document, 'script', 'https://connect.facebook.net/en_US/fbevents.js');
  fbq('init', id);
  fbq('track', 'PageView');
})();

/* Safe wrapper — used by the app to log conversions. Never throws if the pixel
 * is disabled, still loading, or blocked by an ad-blocker. */
window.fbTrack = function (event, params) {
  try { if (window.META_PIXEL_ID && window.fbq) window.fbq('track', event, params || {}); }
  catch (e) { /* no-op */ }
};
