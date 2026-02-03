# src/main.py
import sys

from copy_static import copy_directory
from generate_page import generate_pages_recursive


def normalize_basepath(p: str) -> str:
    if not p:
        return "/"
    if not p.startswith("/"):
        p = "/" + p
    if not p.endswith("/"):
        p += "/"
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
