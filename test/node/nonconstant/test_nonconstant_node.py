import unittest

from src.node.nonconstant.variable_node import VariableNode
from src.node.nonconstant.operations.conjunction_node import ConjunctionNode
from src.node.constant import *


class TestNonConstantNode(unittest.TestCase):
    def setUp(self):
        self.var_a = VariableNode(TrueNode.VALUE)
        self.var_b = VariableNode()
        self.conjunction = ConjunctionNode()
        self.conjunction.left = self.var_a
        self.conjunction.right = self.var_b

    def test_update_value(self):
        self.var_b.value = TrueNode.VALUE
        self.assertEqual(self.conjunction.value, TrueNode.VALUE)

    def test_negation(self):
        self.var_b.negate()
        self.assertEqual(self.conjunction.value, TrueNode.VALUE)

    def test_change_child(self):
        self.conjunction.right = TrueNode()
        self.assertEqual(self.conjunction.value, TrueNode.VALUE)

        self.conjunction.left = FalseNode()
        self.assertEqual(self.conjunction.value, FalseNode.VALUE)
