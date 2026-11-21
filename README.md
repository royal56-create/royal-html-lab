# Royal Web Structure Lab

A practical, offline-first HTML5 learning and development laboratory. It includes a browsable multi-page demo, focused examples, reusable starter templates, accessibility and SEO guidance, and a lightweight validation script.

## Features
- HTML5 document fundamentals, semantic landmarks, links, lists, images, media and tables.
- Multi-page demo site: Home, About, Learning Paths, Templates, Guides and Contact.
- Forms with native controls, labels and browser validation (demo only; no server submission).
- Accessibility examples and checklists.
- SEO metadata examples and best-practice documentation.
- Portfolio, business, landing-page and blog starter templates.
- Dependency-free Python structural checker and GitHub Actions workflow.

## Quick start
1. Clone or download this repository.
2. Open `index.html` in a modern browser.
3. Explore the examples and templates.
4. Run the optional local check: `python scripts/check_html.py`.

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
- Media examples reference optional local files; add media you own or are licensed to use.
- The checker performs basic structural checks, not full standards conformance. Also use the Nu HTML Checker and test with keyboards and assistive technology.

## Contributing and license
See [CONTRIBUTING.md](CONTRIBUTING.md). Released under the MIT License; see [LICENSE](LICENSE).
