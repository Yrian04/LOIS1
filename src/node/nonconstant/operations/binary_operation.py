# Выполнили студенты группы 221701 БГУИР:
# - Глёза Егор Дмитриевич
# - Крупский Артём Викторович
#
# Класс узла бинарной логической операции
# 08.05.2024
#
# Источники:
# - Проектирование программного обеспечения интеллектуальных систем (3 семестр)
#

from abc import ABC

from ..nonconstant_node import OperationNode, NonConstantNode, Node


class BinaryOperation(OperationNode, ABC):
    def __init__(self, value=NonConstantNode.DEFAULT_VALUE):
        super().__init__(value)
        self._right: Node | None = None
        self._left: Node | None = None

    @property
    def left(self) -> Node:
        return self._left

    @left.setter
    def left(self, value: Node):
        if isinstance(self._left, NonConstantNode):
            self._left._remove_parent(self)

        self._left = value

        if isinstance(self._left, NonConstantNode):
            self._left._add_parent(self)

        self.calculate_value()
        self._on_value_changed()

    @property
    def right(self) -> Node:
        return self._right

    @right.setter
    def right(self, value: Node):
        if isinstance(self._right, NonConstantNode):
            self._right._remove_parent(self)

        self._right = value

        if isinstance(self._right, NonConstantNode):
            self._right._add_parent(self)

        self.calculate_value()
        self._on_value_changed()

    def calculate_value(self) -> None:
        if not self.left or not self.right:
            return
        self._value = self._operation(self.left.value, self.right.value)
        self._on_value_changed()

    def _operation(
            self,
            right_value: NonConstantNode.value_type,
            left_value: NonConstantNode.value_type
    ) -> NonConstantNode.value_type: pass

