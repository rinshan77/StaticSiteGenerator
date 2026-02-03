import unittest

from textnode import TextNode, TextType
from split_nodes import split_nodes_image, split_nodes_link


class TestSplitNodes(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_split_images_no_images(self):
        node = TextNode("Just normal text", TextType.TEXT)
        self.assertListEqual([node], split_nodes_image([node]))

    def test_split_images_only_image(self):
        node = TextNode("![alt](https://x.com/a.png)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [TextNode("alt", TextType.IMAGE, "https://x.com/a.png")],
            new_nodes,
        )

    def test_split_images_text_before_and_after(self):
        node = TextNode("Start ![a](u) End", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Start ", TextType.TEXT),
                TextNode("a", TextType.IMAGE, "u"),
                TextNode(" End", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_links_basic(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            ],
            new_nodes,
        )

    def test_split_links_no_links(self):
        node = TextNode("No links here", TextType.TEXT)
        self.assertListEqual([node], split_nodes_link([node]))

    def test_split_links_only_link(self):
        node = TextNode("[x](y)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([TextNode("x", TextType.LINK, "y")], new_nodes)

    def test_non_text_nodes_are_untouched(self):
        node = TextNode("bold", TextType.BOLD)
        self.assertListEqual([node], split_nodes_link([node]))
        self.assertListEqual([node], split_nodes_image([node]))


if __name__ == "__main__":
    unittest.main()

