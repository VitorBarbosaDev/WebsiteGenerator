import unittest
from  htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_eq(self):
        node = HTMLNode("p", "Hello")
        node2 = HTMLNode("p", "Hello")

        self.assertEqual(node, node2)

    def test_not_eq_different_tag(self):
        node = HTMLNode("p", "Hello")
        node2 = HTMLNode("div", "Hello")

        self.assertNotEqual(node, node2)

    def test_not_eq_different_value(self):
        node = HTMLNode("p", "Hello")
        node2 = HTMLNode("p", "World")

        self.assertNotEqual(node, node2)

    def test_not_eq_different_children(self):
        node = HTMLNode("div", "Hello", ["child1"])
        node2 = HTMLNode("div", "Hello", ["child2"])

        self.assertNotEqual(node, node2)

    def test_not_eq_different_props(self):
        node = HTMLNode("div", "Hello", None, {"id": "first"})
        node2 = HTMLNode("div", "Hello", None, {"id": "second"})

        self.assertNotEqual(node, node2)

    def test_default_values(self):
        node = HTMLNode()

        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_props(self):
        props = {"id": "main", "class": "container"}
        node = HTMLNode("div", "Hello", None, props)

        self.assertEqual(node.props, props)

    def test_repr(self):
        node = HTMLNode("p", "Hello")

        expected = "HTMLNode(p, Hello, None,None)"
        self.assertEqual(repr(node), expected)


if __name__ == "__main__":
    unittest.main()
