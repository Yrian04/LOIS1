import unittest

from src.node.nonconstant.operations.negation_node import NegationNode
from src.node.nonconstant import VariableNode as Variable
from src.node.constant import FalseNode, TrueNode


class TestNegativeNode(unittest.TestCase):
    def setUp(self):
        self.node = NegationNode()
        self.node.negated_node = Variable()

    def test_value(self):
        self.assertEqual(self.node.value, TrueNode.VALUE)
        self.node.negated_node.value = TrueNode.VALUE
        self.assertEqual(self.node.value, FalseNode.VALUE)
