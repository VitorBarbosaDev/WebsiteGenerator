from enum import Enum


class TextType(Enum):
    PlainText = ""
    BoldText = "**Bold text**"
    ItalicText = "_Italic text_"
    CodeText = "`Code text`"
    LinkText = "[anchor text](url)"
    ImageText = "![alt text](url)"
            

class TextNode():
    def __init__(self, text: str, text_type: TextType, url: str | None = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return NotImplemented

        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


