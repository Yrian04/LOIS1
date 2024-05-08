# Выполнили студенты группы 221701 БГУИР:
# - Глёза Егор Дмитриевич
# - Крупский Артём Викторович
#
# Классы неконстантного узла и узла операции
# 08.05.2024
#
# Источники:
# - Проектирование программного обеспечения интеллектуальных систем (3 семестр)
#

from abc import ABC, abstractmethod

from ..node import Node
from ..constant import FalseNode


class NonConstantNode(Node, ABC):
    DEFAULT_VALUE: Node.value_type = FalseNode.VALUE

    def __init__(self, value=DEFAULT_VALUE):
        self._value = value
        self._parents: set[OperationNode] = set()

    @property
    def value(self) -> Node.value_type:
        return self._value

    @property
    def parents(self):
        return self._parents.copy()

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


class OperationNode(NonConstantNode, ABC):
    def __init__(self, value=NonConstantNode.DEFAULT_VALUE):
        super().__init__(value)

    @abstractmethod
    def calculate_value(self) -> None: pass
