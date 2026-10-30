import unittest
from  leafnode import LEAFNode

class TestLEAFNode(unittest.TestCase):

    def test_eq(self):
        node = LEAFNode("p", "Hello")
        node2 = LEAFNode("p", "Hello")

        self.assertEqual(node, node2)

    def test_not_eq_different_tag(self):
        node = LEAFNode("p", "Hello")
        node2 = LEAFNode("div", "Hello")

        self.assertNotEqual(node, node2)

    def test_not_eq_different_value(self):
        node = LEAFNode("p", "Hello")
        node2 = LEAFNode("p", "World")

        self.assertNotEqual(node, node2)

    def test_not_eq_different_children(self):
        node = LEAFNode("div", "Hello")
        node2 = LEAFNode("a", "Click me!", {"href": "https://www.google.com"})

        self.assertNotEqual(node, node2)

    def test_not_eq_different_props(self):
        node = LEAFNode("div", "Hello", {"id": "first"})
        node2 = LEAFNode("div", "Hello", {"id": "second"})

        self.assertNotEqual(node, node2)

    def test_default_values(self):
        node = LEAFNode("div", "Hello")

        self.assertIsNotNone(node.tag)
        self.assertIsNotNone(node.value)
        self.assertIsNone(node.props)

    def test_props(self):
        props = {"id": "main", "class": "container"}
        node = LEAFNode("div", "Hello", props)

        self.assertEqual(node.props, props)

    def test_repr(self):
        node = LEAFNode("p", "Hello")

        expected = "LEAFNode(p, Hello,None)"
        self.assertEqual(repr(node), expected)

    def test_leaf_to_html_p(self):
        node = LEAFNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LEAFNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(),'<a href="https://www.google.com">Click me!</a>')
    
    def test_leaf_to_html_multiple_props(self):
        node = LEAFNode(
            "a",
            "Click me!",
            {
                "href": "https://www.google.com",
                "target": "_blank",
                "class": "link"
            }
        )

        expected = '<a href="https://www.google.com" target="_blank" class="link">Click me!</a>'
        self.assertEqual(node.to_html(), expected)

    def test_leaf_to_html_empty_props(self):
        node = LEAFNode("p", "Hello", {})

        self.assertEqual(node.to_html(), "<p>Hello</p>")

    def test_leaf_to_html_none_tag(self):
        node = LEAFNode(None, "Hello")

        self.assertEqual(node.to_html(), "Hello")

    def test_leaf_to_html_none_value(self):
        node = LEAFNode("p", None)

        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_has_no_children(self):
        node = LEAFNode("div", "Hello")

        self.assertIsNone(node.children)

    def test_leaf_to_html_special_characters(self):
        node = LEAFNode("p", "Hello & Goodbye")

        self.assertEqual(
            node.to_html(),
            "<p>Hello & Goodbye</p>"
        )


if __name__ == "__main__":
    unittest.main()
