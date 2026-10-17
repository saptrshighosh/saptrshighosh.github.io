# Saptrshi Ghosh — ML & AI portfolio

Live site: https://saptrshighosh.github.io/

A lightweight, responsive portfolio for machine-learning research and applied AI opportunities. Five static HTML pages; no framework, package installation, tracking, or runtime API keys.

## Structure

- `index.html` — overview and selected work
- `projects.html` — complete project catalog, category filters, and search
- `research.html` — experience, research methods, manuscripts, and presentations
- `background.html` — education, skills, training, teaching, awards, and service
- `contact.html` — contact information and areas of interest
- `assets/` — shared CSS, progressive-enhancement JavaScript, content data, and favicon
- `profile.jpg` — the sole content image, retained at its existing URL
- `tools/build.py` — standard-library Python generator
- `tools/check.py` — internal links, image, HTML, and content checks
- `robots.txt`, `sitemap.xml`, `.nojekyll` — static hosting and discovery

## Update content

Edit project, skill, and training records in `assets/content.json`. Edit page narratives in `tools/build.py`. Then run:

```sh
python3 tools/build.py
python3 tools/check.py
python3 -m http.server 8765
```

Open http://localhost:8765/ to preview. Commit the generated HTML alongside the source so GitHub Pages can serve the site from the root of `main` without a build service.

Set a project’s `public` flag to true only after its repository is publicly accessible. Course links are labeled as courses; issuer credential links are labeled as credentials.

## Content conventions

- PhD **student**, Jan 2026–present; expected May 2030.
- MS **Mechanical Engineering**, Aug 2023–May 2025; GPA 4.0/4.0.
- BTech original CGPA **8.57/10**; no unexplained conversion.
- The 95% result is four-cell-line research classification, with biological sample-level splitting and training-only fitting; not a clinical diagnostic claim.
- Both manuscripts are submitted and under revision. The associated IP is an invention disclosure with OU OTC; no unconfirmed patent-filing claim.
- LLM project work, completed training, and future research interests are described separately.
- Private transcripts, draft recommendations, and job-specific application documents are not website assets.
- The profile portrait is the only content image.

## Hosting

GitHub Pages serves these static files. Preserve `research.html`, `projects.html`, and `contact.html` when changing navigation because existing applications link to them.

Source code license: see LICENSE. Personal photograph and biographical content remain attributable to Saptrshi Ghosh.
