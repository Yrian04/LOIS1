from abc import ABC

from ..node import Node


class ConstantNode(Node, ABC):
    VALUE: Node.value_type

    @property
    def value(self) -> Node.value_type:
        return self.VALUE

