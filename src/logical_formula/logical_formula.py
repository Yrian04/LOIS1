# Выполнили студенты группы 221701 БГУИР:
# - Глёза Егор Дмитриевич
# - Крупский Артём Викторович
#
# Класс логической формулы
# 08.05.2024
#
# Источники:
# - Проектирование программного обеспечения интеллектуальных систем (3 семестр)
#

from ..node import Node
from ..node.nonconstant.variable_node import VariableNode as Variable
from ..node.nonconstant.operations import BinaryOperation, NegationNode as Negation
from ..node.constant import ConstantNode as Constant


class LogicalFormula:
    value_type = Node.value_type

    def __init__(self, root: Node | None = None):
        self._root = root
        self._vars: list[Variable] = []

        stack = [self._root]
        while stack:
            node = stack.pop()
            match node:
                case Variable():
                    if node not in self._vars:
                        self._vars.append(node)
                case BinaryOperation():
                    stack.append(node.left)
                    stack.append(node.right)
                case Negation():
                    stack.append(node.negated_node)
                case None:
                    continue

    @property
    def value(self) -> value_type:
        return self._root.value

    @property
    def variables(self) -> list[Variable]:
        return self._vars.copy()

    def fix_variable(self, variable: Variable, value: Constant) -> None:
        if variable not in self._vars:
            raise KeyError(self)
        self._vars.remove(variable)

        for parent in variable.parents:
            match parent:
                case BinaryOperation():
                    if parent.left is variable:
                        parent.left = value
                    if parent.right is variable:
                        parent.right = value
                case Negation():
                    parent.negated_node = value
