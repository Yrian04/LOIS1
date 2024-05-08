import unittest

from src.logical_formula.logical_formula_parser import LogicalFormulaParser
from src.logical_formula.token import Token
from src.node.nonconstant import operations
from src.node.nonconstant.variable_node import VariableNode as Variable
from src.node.constant import TrueNode, FalseNode


class TestLogicalFormulaParser(unittest.TestCase):
    def setUp(self):
        self.parser = LogicalFormulaParser()

    def test_parse(self):
        root = self.parser.parse([
            Token.left_bracket,
            Token.left_bracket,
            Token.negation,
            Token.left_bracket,
            'A',
            Token.conjunction,
            'B',
            Token.right_bracket,
            Token.right_bracket,
            Token.disjunction,
            Token.left_bracket,
            Token.left_bracket,
            Token.false,
            Token.implication,
            'B',
            Token.right_bracket,
            Token.equivalence,
            Token.true,
            Token.right_bracket,
            Token.right_bracket,
        ])
        self.assertIsInstance(root, operations.DisjunctionNode)

        self.assertIsInstance(root.left, operations.NegationNode)

        self.assertIsInstance(root.left.negated_node, operations.ConjunctionNode)

        self.assertIsInstance(root.left.negated_node.left, Variable)
        self.assertIsInstance(var_b := root.left.negated_node.right, Variable)

        self.assertIsInstance(root.right, operations.EquivalenceNode)

        self.assertIsInstance(root.right.left, operations.ImplicationNode)

        self.assertIs(root.right.left.left, FalseNode())

        self.assertIs(root.right.left.right, var_b)

        self.assertIs(root.right.right, TrueNode())

