# Выполнили студенты группы 221701 БГУИР:
# - Глёза Егор Дмитриевич
# - Крупский Артём Викторович
#
# Класс константного узла
# 08.05.2024
#
# Источники:
# - Проектирование программного обеспечения интеллектуальных систем (3 семестр)
#

from abc import ABC

from ..node import Node


class ConstantNode(Node, ABC):
    VALUE: Node.value_type

    @property
    def value(self) -> Node.value_type:
        return self.VALUE

