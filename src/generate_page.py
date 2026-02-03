# src/generate_page.py
import os
from markdown_to_html import markdown_to_html_node


def extract_title(markdown: str) -> str:
    for line in markdown.splitlines():
        s = line.strip()
        if s.startswith("# "):
            return s[2:].strip()
    raise Exception("No h1 header found")


def generate_page(
    from_path: str, template_path: str, dest_path: str, basepath: str = "/"
) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r", encoding="utf-8") as f:
        markdown = f.read()

    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    content_html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    full_html = template.replace("{{ Title }}", title).replace(
        "{{ Content }}", content_html
    )

    full_html = full_html.replace('href="/', f'href="{basepath}')
    full_html = full_html.replace('src="/', f'src="{basepath}')

    os.makedirs(os.path.dirname(dest_path) or ".", exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(full_html)


def generate_pages_recursive(
    dir_path_content: str, template_path: str, dest_dir_path: str, basepath: str = "/"
) -> None:
    os.makedirs(dest_dir_path, exist_ok=True)

    for entry in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, entry)

        if os.path.isdir(src_path):
            generate_pages_recursive(
                src_path,
                template_path,
                os.path.join(dest_dir_path, entry),
                basepath,
            )
            continue

        if os.path.isfile(src_path) and entry.endswith(".md"):
            out_name = entry[:-3] + ".html"
            dest_path = os.path.join(dest_dir_path, out_name)
            generate_page(src_path, template_path, dest_path, basepath)
