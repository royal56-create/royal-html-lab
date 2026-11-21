#!/usr/bin/env python3
"""Dependency-free basic structural checks for repository HTML files."""
from html.parser import HTMLParser
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
VOID = {"area","base","br","col","embed","hr","img","input","link","meta","param","source","track","wbr"}

class Checker(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack=[]; self.errors=[]; self.doctype=False
        self.lang=False; self.charset=False; self.title=False; self.ids=set()
    def handle_decl(self, decl):
        if decl.lower()=="doctype html": self.doctype=True
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if tag=="html" and attrs.get("lang"): self.lang=True
        if tag=="meta" and attrs.get("charset"): self.charset=True
        if tag=="title": self.title=True
        if attrs.get("id"):
            ident=attrs["id"]
            if ident in self.ids: self.errors.append(f"duplicate id: {ident}")
            self.ids.add(ident)
        if tag=="img" and "alt" not in attrs: self.errors.append("img missing alt attribute")
        if tag not in VOID: self.stack.append(tag)
    def handle_endtag(self, tag):
        if tag in VOID: return
        if tag not in self.stack:
            self.errors.append(f"unexpected closing tag: </{tag}>"); return
        if self.stack[-1]!=tag:
            self.errors.append(f"misnested closing tag: </{tag}> (expected </{self.stack[-1]}>)")
            while self.stack and self.stack[-1]!=tag: self.stack.pop()
        if self.stack and self.stack[-1]==tag: self.stack.pop()
    def finish(self):
        self.close()
        if not self.doctype: self.errors.append("missing <!doctype html>")
        if not self.lang: self.errors.append("missing html lang attribute")
        if not self.charset: self.errors.append("missing meta charset")
        if not self.title: self.errors.append("missing title element")
        if self.stack: self.errors.append("unclosed elements: "+", ".join(self.stack))

def main():
    paths=sorted(ROOT.rglob("*.html")); failures=0
    for path in paths:
        checker=Checker()
        try:
            checker.feed(path.read_text(encoding="utf-8")); checker.finish()
        except Exception as exc: checker.errors.append(f"parser error: {exc}")
        if checker.errors:
            failures+=1; print("FAIL",path.relative_to(ROOT))
            for error in checker.errors: print("  -",error)
        else: print("PASS",path.relative_to(ROOT))
    print(f"\nChecked {len(paths)} HTML files; {failures} failed.")
    return 1 if failures else 0

if __name__=="__main__": sys.exit(main())
