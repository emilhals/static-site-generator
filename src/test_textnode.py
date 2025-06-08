import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.LINK, "https://www.boot.dev/lessons/0abc7ce4-3855-4624-9f2d-7e566690fee1")
        node4 = TextNode("This is a text node", TextType.LINK, "https://developer.mozilla.org/en-US/docs/Glossary/Inline-level_content")
        self.assertEqual(node, node2)
        self.assertEqual(node3, node4)
        self.assertNotEqual(node, node3)

if __name__ == "__main__":
    unittest.main()
