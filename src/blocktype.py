from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block):
    lines = block.split("\n")

    if lines and lines[0].startswith("#"):
        i = 0
        while i < len(lines[0]) and lines[0][i] == "#":
            i += 1
        if 1 <= i <= 6 and len(lines[0]) > i and lines[0][i] == " ":
            return BlockType.HEADING

    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE

    if lines and all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    if lines and all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    if lines:
        expected = 1
        ok = True
        for line in lines:
            prefix = f"{expected}. "
            if not line.startswith(prefix):
                ok = False
                break
            expected += 1
        if ok:
            return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
