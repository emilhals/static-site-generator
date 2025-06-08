import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_single_prop(self):
        node = HTMLNode("a", "This is a HTML node", None, {"target": "_blank"})
        expected = 'target="_blank"'

        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_multiple_props(self):
        node = HTMLNode("a", "This is a HTML node", None, {"href": "https://www.google.com", "target": "_blank"})
        expected = 'href="https://www.google.com" target="_blank"'

        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_empty(self):
        node2 = HTMLNode("a", "This is a HTML node")
        with self.assertRaises(ValueError):
            node2.props_to_html()

if __name__ == "__main__":
    unittest.main()

