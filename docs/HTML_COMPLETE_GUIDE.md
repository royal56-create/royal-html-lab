# HTML Complete Guide

This guide is a structured roadmap for the Royal Web Structure Lab. Use the linked examples as practical references; it is not a replacement for the WHATWG HTML Living Standard.

## 1. Document foundations
- `<!doctype html>`, `html`, `head`, `body`, `title`, `meta`.
- Character encoding, viewport, language and page title.
- See [document fundamentals](../examples/fundamentals/document.html).

## 2. Text and page structure
- Headings `h1` `h6`, paragraphs, emphasis, quotations, code, lists and description lists.
- Semantic landmarks: `header`, `nav`, `main`, `section`, `article`, `aside`, `footer`.
- Use headings in a logical hierarchy; do not choose elements only for their default appearance.

## 3. Links, images and media
- Links, fragment identifiers, download links and safe external-link attributes.
- Images with meaningful `alt`, responsive `srcset` and `sizes`, `picture` and `source`.
- Audio, video, captions, tracks, SVG and Canvas.
- See [responsive images](../examples/media/responsive-images.html), [SVG](../examples/graphics/svg-basics.html) and [Canvas](../examples/graphics/canvas-basics.html).

## 4. Forms and controls
- `form`, `label`, `input`, `textarea`, `select`, `option`, `button`.
- Input types: text, email, password, number, date, time, file, color, range, URL and search.
- Constraints: required, min, max, minlength, maxlength, pattern and step.
- Suggestions with `datalist`, calculated values with `output`, grouped controls with `fieldset` and `legend`.
- Browser validation improves usability but never replaces server-side validation.
- See [form validation](../examples/forms/form-validation.html), [datalist and output](../examples/forms/datalist-output.html) and [advanced controls](../examples/forms/advanced-form-controls.html).

## 5. Tables and structured data
- Use `table`, `caption`, `thead`, `tbody`, `tr`, `th` and `td` for tabular data, not page layout.
- Associate headers using `scope` where appropriate.
- Use JSON-LD only when it accurately describes visible page content.

## 6. Interactive and embedded elements
- `details` / `summary`, `dialog`, `template`, `progress` and `meter`.
- Iframes, `srcdoc`, sandbox permissions, lazy loading and descriptive titles.
- Drag and drop requires a keyboard-accessible alternative.

## 7. Accessibility
- Prefer native semantic HTML and controls.
- Provide text alternatives, labels, captions, visible focus, sufficient contrast and logical reading order.
- Use ARIA only to fill genuine semantic gaps; test with keyboard and assistive technology.
- See [accessibility examples](../examples/accessibility/aria-keyboard-patterns.html).

## 8. SEO, metadata and security
- Unique titles, useful descriptions, canonical URLs, Open Graph and social card metadata.
- Use HTTPS, safe output handling, restrictive iframe permissions and server security headers.
- Never treat client-side validation as a security boundary.
- See [metadata example](../examples/seo/open-graph-metadata.html) and [security patterns](../examples/security/secure-html-patterns.html).

## 9. Quality checklist
1. Validate markup with the Nu HTML Checker.
2. Run `python scripts/check_html.py`.
3. Check all local links, image paths and page titles.
4. Test at narrow and wide viewport sizes.
5. Navigate every control using only a keyboard.
6. Test accessible names and reading order with assistive technology.
7. Verify external links, embedded content and metadata before publishing.

## Reference
- [WHATWG HTML Living Standard](https://html.spec.whatwg.org/)
- [MDN HTML documentation](https://developer.mozilla.org/docs/Web/HTML)
- [W3C Nu HTML Checker](https://validator.w3.org/nu/)
