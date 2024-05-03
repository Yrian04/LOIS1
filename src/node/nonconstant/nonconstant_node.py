from abc import ABC, abstractmethod

from ..node import Node
from ..constant import FalseNode


class NonConstantNode(Node, ABC):
    DEFAULT_VALUE: Node.value_type = FalseNode.VALUE

    def __init__(self, value=DEFAULT_VALUE, is_negative=False):
        self._value = value
        self._parents: set[OperationNode] = set()
        self._is_negative = is_negative

    @property
    def value(self) -> Node.value_type:
        return self.__negation() if self._is_negative else self._value

    @property
    def parents(self):
        return self._parents.copy()

    @property
    def is_negative(self):
        return self._is_negative

    def negate(self):
        self._is_negative = not self._is_negative
        self._on_value_changed()

    def _add_parent(self, parent: "OperationNode"):
        self._parents.add(parent)

    def _remove_parent(self, parent: "OperationNode"):
        try:
            self._parents.remove(parent)
        except KeyError as e:
            raise ValueError(e)

    def _on_value_changed(self):
        for parent in self.parents:
            parent.calculate_value()

    def __negation(self) -> Node.value_type:
        return not self._value


class OperationNode(NonConstantNode, ABC):
    def __init__(self, value=NonConstantNode.DEFAULT_VALUE, *, is_negative=False):
        super().__init__(value, is_negative=is_negative)
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

    @abstractmethod
    def _operation(
            self,
            right_value: NonConstantNode.value_type,
            left_value: NonConstantNode.value_type
    ) -> NonConstantNode.value_type: pass
