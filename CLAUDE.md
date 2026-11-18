# Agent notes

- Research spikes go in `research/<topic>/`. Follow the layout and rules in [research/README.md](research/README.md): committed WebP images only, third-party images in `img/third-party/<website>/` with a CREDITS.md row each, and downloads in a gitignored `.cache/`. Run `python research/check-images.py` before committing.
- Models built from scans go in `models/<name>/` with a README that separates what was measured from what was assumed, and a `metrics.json` of the measured numbers.
- This repo publishes results only: scans, model files, measurements, pictures and research pages. Do not commit how they are made: no build or analysis scripts, no modelling plans or recommendations, no step-by-step method notes, and no story or video work. The one script here is `research/check-images.py`, which checks pages.
