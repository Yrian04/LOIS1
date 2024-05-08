# Выполнили студенты группы 221701 БГУИР:
# - Глёза Егор Дмитриевич
# - Крупский Артём Викторович
#
# Перечисление токенов для лексера
# 08.05.2024
#
# Источники:
# - Проектирование программного обеспечения интеллектуальных систем (3 семестр)
#

import enum


class Token(enum.Enum):
    conjunction = 0
    disjunction = 1
    implication = 2
    equivalence = 3
    negation = 4
    left_bracket = 5
    right_bracket = 6
    true = 7
    false = 8
