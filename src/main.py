# src/main.py
import sys

from copy_static import copy_directory
from generate_page import generate_pages_recursive


def normalize_basepath(p: str) -> str:
    # default
    if not p:
        return "/"
    # ensure leading slash
    if not p.startswith("/"):
        p = "/" + p
    # ensure trailing slash (GitHub Pages wants "/REPO/")
    if not p.endswith("/"):
        p += "/"
    # collapse accidental "//"
    if p == "//":
        p = "/"
    return p


def main():
    basepath = normalize_basepath(sys.argv[1]) if len(sys.argv) > 1 else "/"

    out_dir = "docs"

    copy_directory("static", out_dir)
    generate_pages_recursive("content", "template.html", out_dir, basepath)


if __name__ == "__main__":
    main()
