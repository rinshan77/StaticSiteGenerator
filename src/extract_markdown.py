import re


def extract_markdown_images(text):
    # ![alt text](url)
    # capture alt text and url as groups
    pattern = r"!\[([^\]]*)\]\(([^)]+)\)"
    return re.findall(pattern, text)


def extract_markdown_links(text):
    # [anchor](url) but NOT preceded by !
    pattern = r"(?<!\!)\[([^\]]*)\]\(([^)]+)\)"
    return re.findall(pattern, text)

