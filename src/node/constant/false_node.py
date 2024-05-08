# Выполнили студенты группы 221701 БГУИР:
# - Глёза Егор Дмитриевич
# - Крупский Артём Викторович
#
# Класс узла для константы ложь
# 08.05.2024
#
# Источники:
# - Проектирование программного обеспечения интеллектуальных систем (3 семестр)
#

from .constant_node import ConstantNode
from src.singleton import singleton


@singleton
class FalseNode(ConstantNode):
    VALUE = False
