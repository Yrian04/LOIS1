# Выполнили студенты группы 221701 БГУИР:
# - Глёза Егор Дмитриевич
# - Крупский Артём Викторович
#
# Класс узла для конъюнкции
# 08.05.2024
#
# Источники:
# - Проектирование программного обеспечения интеллектуальных систем (3 семестр)
#

from .binary_operation import BinaryOperation


class ConjunctionNode(BinaryOperation):
    def _operation(self, right_value: BinaryOperation.value_type,
                   left_value: BinaryOperation.value_type) -> BinaryOperation.value_type:
        return right_value & left_value
