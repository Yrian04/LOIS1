# Выполнили студенты группы 221701 БГУИР:
# - Глёза Егор Дмитриевич
# - Крупский Артём Викторович
#
# Класс для хранения тестов, относящихся к классу узлов дизъюнкций
# 08.05.2024
#
# Источники:
# - Проектирование программного обеспечения интеллектуальных систем (3 семестр)
#

import unittest

from src.node.nonconstant.operations import DisjunctionNode
from src.node.constant import TrueNode, FalseNode


class TestDisjunctionNode(unittest.TestCase):
    def setUp(self):
        self.node = DisjunctionNode()
        self.node.left = FalseNode()
        self.node.right = FalseNode()
        self.node.calculate_value()

    def test_disjunction(self):
        self.assertEqual(self.node.value, FalseNode.VALUE)

        self.node.left = TrueNode()
        self.node.calculate_value()
        self.assertEqual(self.node.value, TrueNode.VALUE)

        self.node.right = TrueNode()
        self.node.calculate_value()
        self.assertEqual(self.node.value, TrueNode.VALUE)

        self.node.left = FalseNode()
        self.node.calculate_value()
        self.assertEqual(self.node.value, TrueNode.VALUE)


if __name__ == "__main__":
    unittest.main()

