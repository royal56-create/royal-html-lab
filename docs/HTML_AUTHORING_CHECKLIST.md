# HTML Authoring Checklist

Use this checklist before publishing a page.

## Document basics
- [ ] Include `<!doctype html>`.
- [ ] Set the correct document language on `<html lang="...">`.
- [ ] Include UTF-8 charset and a responsive viewport declaration.
- [ ] Give the page a unique, descriptive `<title>`.
- [ ] Write a useful meta description where appropriate.

## Structure and content
- [ ] Use one clear page-level `<h1>` and a logical heading hierarchy.
- [ ] Use `<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>` and `<footer>` according to meaning.
- [ ] Use lists for grouped list content and tables only for tabular data.
- [ ] Ensure links describe their destination and buttons describe their action.
- [ ] Avoid using elements only for their default visual appearance.

## Images and media
- [ ] Provide appropriate `alt` text for images.
- [ ] Use `alt=""` for decorative images.
- [ ] Include width and height attributes when known.
- [ ] Add captions or transcripts when needed for media.
- [ ] Use responsive image sources for large or varied layouts.

## Forms
- [ ] Associate every form control with a visible label.
- [ ] Group related controls with `fieldset` and `legend` where appropriate.
- [ ] Choose the correct input type and autocomplete value.
- [ ] Explain required formats and constraints.
- [ ] Never rely on client-side validation alone for a real server application.

## Accessibility and quality
- [ ] Check keyboard navigation and visible focus.
- [ ] Check color contrast and zoom/reflow.
- [ ] Avoid positive tabindex values.
- [ ] Check unique IDs and valid fragment links.
- [ ] Test at narrow and wide viewport sizes.
- [ ] Run the repository checker and a standards-based HTML validator.
- [ ] Test with at least one screen reader when possible.

## Before release
- [ ] Remove placeholder text and sample data.
- [ ] Confirm every internal link and asset path works.
- [ ] Confirm no secrets or private data are committed.
- [ ] Review the page in more than one browser.
