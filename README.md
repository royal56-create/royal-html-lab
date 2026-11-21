# Royal Web Structure Lab

> **Educational / demo use only:** Review code before running it. Use only on files, devices, repositories, and networks you own or are explicitly authorized to access. Use at your own risk; no warranty is provided to the maximum extent permitted by applicable law. This notice does not waive non-waivable legal rights or obligations.
A practical, offline-first HTML5 learning and development laboratory. It includes a browsable multi-page demo, focused examples, reusable starter templates, accessibility and SEO guidance, and a lightweight validation script.

## Features
- HTML5 document fundamentals, semantic landmarks, links, lists, images, media, tables and forms.
- Practical examples for Canvas, SVG, dialog, template, progress, meter, iframe and drag-and-drop.
- Native form controls, validation, datalist, output and accessible form patterns.
- Accessibility guidance for keyboard use, ARIA, labels and live regions.
- SEO metadata, Open Graph, JSON-LD and safer HTML patterns.
- Multi-page demo site and portfolio, business, landing-page and blog starter templates.
- Dependency-free Python structural checker and GitHub Actions workflow.

## Quick start
1. Clone or download this repository.
2. Open `index.html` in a modern browser.
3. Explore `examples/`, `templates/` and `docs/`.
4. Read [the complete HTML guide](docs/HTML_COMPLETE_GUIDE.md).
5. Run the optional local check: `python scripts/check_html.py`.

No package installation, API key, backend, external CDN or third-party runtime service is required.

## Structure
```text
pages/       Multi-page demo site
examples/    Focused HTML examples by topic
templates/   Reusable starter page structures
assets/      Local CSS and SVG assets
docs/        Guides and reference material
scripts/     Local quality checker
.github/     GitHub Actions workflow
```

## Important limitations
- This is a static learning project, not a hosted application.
- The contact and login examples do not authenticate users or send/store data.
- Media examples may reference optional local files; add media you own or are licensed to use.
- The checker performs basic structural checks, not full standards conformance. Also use the [Nu HTML Checker](https://validator.w3.org/nu/) and test with keyboards and assistive technology.

## Contributing and license
See [CONTRIBUTING.md](CONTRIBUTING.md). Released under the MIT License; see [LICENSE](LICENSE).
