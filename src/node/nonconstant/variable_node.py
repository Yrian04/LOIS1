# Выполнили студенты группы 221701 БГУИР:
# - Глёза Егор Дмитриевич
# - Крупский Артём Викторович
#
# Класс узла, обозначающего переменную
# 08.05.2024
#
# Источники:
# - Проектирование программного обеспечения интеллектуальных систем (3 семестр)
#

from .nonconstant_node import NonConstantNode


class VariableNode(NonConstantNode):
    @NonConstantNode.value.setter
    def value(self, value: NonConstantNode.value_type):
        self._value = value
        self._on_value_changed()

    def negate_value(self):
        self._value = not self._value
        self._on_value_changed()
