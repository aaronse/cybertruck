# Research

Each folder here is a short research spike into one part or question. A spike usually starts from an issue, for example [#1, the passenger mirror lower cover](https://github.com/aaronse/cybertruck/issues/1).

| Topic | Started from | Status |
|---|---|---|
| [Exterior side mirrors](exterior-side-mirrors/) | [#1](https://github.com/aaronse/cybertruck/issues/1) | Research done. [Multi-part model](../models/exterior-side-mirror/) built from our scan: outer shells only. Needs clip geometry and a scale check from a real mirror. |

## Folder layout

```
research/<topic>/
  README.md                  the page itself
  <name>.md                  further pages on the same topic, under the same rules
  img/                       images we made (scan renders, sketches), as .webp
  img/third-party/
    CREDITS.md               one row per file: what it shows, original URL, owner, post or page
    <website>/<name>.webp    copies of other people's images, grouped by source website
  .cache/                    gitignored: full-size originals, downloaded models, raw pages
```

## Rules for research pages

1. **A clone must render the page with no network access.** Every image the page shows is a committed `.webp` under the topic's `img/`, referenced by a relative path. Never hotlink, and never link into `.cache/`.
2. **Mark third-party images and credit them.** Copies go in `img/third-party/<website>/`, using the bare domain as the folder name (`service.tesla.com`, `tesery.com`). Name each file for what it shows, not by the source's id. Add a row to `img/third-party/CREDITS.md` for each file.
3. **Resize to at most 1200 px wide.** WebP quality 80 suits photos and 90 suits screenshots with text. Keep the full-size original in `.cache/`.
4. **Back every claim with a dated source.** Each claim links to a numbered entry in the page's Sources list. Label inferences and unverified items as such.
5. **Keep downloaded models in `.cache/` until we decide what can live in the repo.** The page lists each cached file with its source and licence.

Models built from research go in `models/<name>/`, with a README under the same image rules.

Run `python research/check-images.py` before committing. It covers `research/` and `models/`. It fails on remote or missing images, non-WebP files, uncommitted files, links into `.cache/`, and third-party files missing from CREDITS.md.
