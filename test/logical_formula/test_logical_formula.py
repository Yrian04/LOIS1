# Выполнили студенты группы 221701 БГУИР:
# - Глёза Егор Дмитриевич
# - Крупский Артём Викторович
#
# Класс для хранения тестов для класса логической формулы
# 08.05.2024
#
# Источники:
# - Проектирование программного обеспечения интеллектуальных систем (3 семестр)
#

import unittest

from src.logical_formula.logical_formula import LogicalFormula
from src.node.nonconstant.variable_node import VariableNode as Variable
from src.node.nonconstant.operations import *
from src.node.constant import TrueNode, FalseNode


class TestLogicalFormula(unittest.TestCase):
    def setUp(self):
        self.var_a = Variable(TrueNode.VALUE)
        self.var_b = Variable()
        self.var_c = Variable()
        self.negation = NegationNode()
        self.negation.negated_node = self.var_b
        self.root = ConjunctionNode()
        self.root.left = self.var_a
        self.disjunction = DisjunctionNode()
        self.root.right = self.disjunction
        self.disjunction.left = self.negation
        self.disjunction.right = self.var_c
        self.formula = LogicalFormula(self.root)

    def test_init(self):
        self.assertIn(self.var_a, self.formula.variables)
        self.assertIn(self.var_b, self.formula.variables)
        self.assertIn(self.var_c, self.formula.variables)

    def test_value(self):
        self.assertEqual(self.formula.value, TrueNode.VALUE)

    def test_fix_variable(self):
        self.formula.fix_variable(self.var_b, TrueNode())
        self.assertEqual(self.negation.negated_node, TrueNode())
        self.assertNotIn(self.var_b, self.formula.variables)
        self.assertEqual(self.formula.value, FalseNode.VALUE)

        self.formula.fix_variable(self.var_c, TrueNode())
        self.assertEqual(self.negation.negated_node, TrueNode())
        self.assertNotIn(self.var_c, self.formula.variables)
        self.assertEqual(self.formula.value, TrueNode.VALUE)

        self.assertRaises(KeyError, self.formula.fix_variable, Variable(), TrueNode())

