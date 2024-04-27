import unittest

from src.node.nonconstant.operations import EquivalenceNode
from src.node.constant import TrueNode, FalseNode


class TestEquivalenceNode(unittest.TestCase):
    def setUp(self):
        self.node = EquivalenceNode()
        self.node.left = FalseNode()
        self.node.right = FalseNode()
        self.node.calculate_value()

    def test_equivalence(self):
        self.assertEqual(self.node.value, TrueNode.VALUE)

        self.node.left = TrueNode()
        self.node.calculate_value()
        self.assertEqual(self.node.value, FalseNode.VALUE)

        self.node.right = TrueNode()
        self.node.calculate_value()
        self.assertEqual(self.node.value, TrueNode.VALUE)

        self.node.left = FalseNode()
        self.node.calculate_value()
        self.assertEqual(self.node.value, FalseNode.VALUE)


if __name__ == "__main__":
    unittest.main()

