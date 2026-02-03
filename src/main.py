from textnode import TextNode, TextType


def main():
    node = TextNode("this is example", TextType.LINK, "www.eatme.ass")
    print(node)


main()
