from htmlnode import *

class LeafNode(HTMLNode):
    def __init__(self, tag, value) -> None:
        super().__init__(tag, value)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("LeafNode must have a value!")
        if self.tag is None:
            return self.value

        return f"<{self.tag}>{self.value}</{self.tag}>"
