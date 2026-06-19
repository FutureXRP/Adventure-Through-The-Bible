# Storybook illustrations

This folder holds the page illustrations for the **Read the Storybook** reader —
a page-turning picture-book view that plays inside each story's existing audio
narration (same voice, same word-by-word highlighting).

## How it works

- A story opts in by adding a `storybook` block to its entry in `stories.json`
  (Tier 1, ages 9–12) or `stories-tier2.json` (Tier 2, ages 5–8):

  ```json
  "storybook": {
    "images": [
      "./storybook/creation/01.webp",
      "./storybook/creation/02.webp"
    ]
  }
  ```

- **One image per story paragraph, in order.** `images[0]` illustrates the first
  paragraph, `images[1]` the second, and so on. The reader shows one paragraph
  per page, so the image count should match the paragraph count for that story
  **in that tier** (paragraph counts differ between Tier 1 and Tier 2, so each
  tier keeps its own image set).

- The narration drives the book: as the audio reaches a new paragraph the page
  turns automatically and the spoken word highlights. Turning a page by hand
  (arrows, tapping the left/right edge, swiping, or the ← → keys) seeks the
  narration to that page.

- **Missing images degrade gracefully.** Until a `.webp` exists at its path, that
  page shows a styled "Illustration coming soon" placeholder, so the reader is
  fully usable while art is still in production. Drop the file in at the right
  path and it appears — no code change needed.

## File convention

```
storybook/<story-id>/NN.webp     e.g. storybook/creation/01.webp
```

- `<story-id>` is the story's `id` field (e.g. `creation`, `noah`, `david-goliath`).
- `NN` is the zero-padded paragraph number (`01`, `02`, …).

## Recommended image specs

- **Format:** WebP (best size/quality; the service worker caches it for offline).
- **Aspect:** landscape ~4:3 (e.g. 1200×900). The frame uses `object-fit: cover`.
- **Weight:** keep each under ~300 KB so the whole library stays light on
  GitHub Pages. If the collection grows large, move images to Supabase Storage
  (already in the stack, CDN-backed) and point the JSON paths there.
- **Style:** one consistent art style across the whole library, with reference
  sheets for recurring characters (Moses, David, Jesus) so they look the same
  from story to story. Review every image for accuracy and reverence.
