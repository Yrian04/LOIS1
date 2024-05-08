# Выполнили студенты группы 221701 БГУИР:
# - Глёза Егор Дмитриевич
# - Крупский Артём Викторович
#
# Класс узла синтаксического дерева для логического выражения
# 08.05.2024
#
# Источники:
# - Проектирование программного обеспечения интеллектуальных систем (3 семестр)
#

from abc import ABC, abstractmethod


class Node(ABC):
    value_type = bool | None

    @property
    @abstractmethod
    def value(self) -> value_type: pass
