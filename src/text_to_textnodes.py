from textnode import TextNode, TextType
from split_nodes import split_nodes_image, split_nodes_link
from split_delimiter import split_nodes_delimiter 


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]

    # order matters
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)

    return nodes
