from ..node import Node
from ..node.nonconstant.variable_node import VariableNode as Variable
from ..node.nonconstant.nonconstant_node import OperationNode as Operation
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
                    self._vars.append(node)
                case Operation():
                    stack.append(node.left)
                    stack.append(node.right)
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
            if parent.left is variable:
                parent.left = value
            if parent.right is variable:
                parent.right = value
