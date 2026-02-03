from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links


def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        # only split TEXT nodes
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        matches = extract_markdown_images(text)

        # no images -> keep node as-is
        if not matches:
            new_nodes.append(node)
            continue

        for alt, url in matches:
            markdown = f"![{alt}]({url})"
            parts = text.split(markdown, 1)

            if len(parts) != 2:
                raise Exception("Invalid markdown image syntax")

            before, after = parts

            if before != "":
                new_nodes.append(TextNode(before, TextType.TEXT))

            new_nodes.append(TextNode(alt, TextType.IMAGE, url))

            text = after  # keep splitting the remainder

        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        # only split TEXT nodes
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        matches = extract_markdown_links(text)

        # no links -> keep node as-is
        if not matches:
            new_nodes.append(node)
            continue

        for anchor, url in matches:
            markdown = f"[{anchor}]({url})"
            parts = text.split(markdown, 1)

            if len(parts) != 2:
                raise Exception("Invalid markdown link syntax")

            before, after = parts

            if before != "":
                new_nodes.append(TextNode(before, TextType.TEXT))

            new_nodes.append(TextNode(anchor, TextType.LINK, url))

            text = after

        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes

