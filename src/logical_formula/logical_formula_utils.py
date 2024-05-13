# Выполнили студенты группы 221701 БГУИР:
# - Глёза Егор Дмитриевич
# - Крупский Артём Викторович
#
# Модуль для утилит, связанных с логическими выражениями
# 08.05.2024
#
# Источники:
# - Проектирование программного обеспечения интеллектуальных систем (3 семестр)
#

import math

from .logical_formula import LogicalFormula
from .logical_formula_lexer import LogicalFormulaLexer as Lexer
from .logical_formula_parser import LogicalFormulaParser as Parser


def get_logical_formula_from_string(
        string: str,
        lexer=Lexer(),
        parser=Parser()
) -> LogicalFormula:
    tokens = lexer.analyze(string)
    root = parser.parse(tokens)
    return LogicalFormula(root)


def is_formula_impossible(formula: LogicalFormula) -> bool:
    def to_gray(n: int):
        return n ^ (n << 1)

    if formula.value:
        return False

    prev_grey = 0
    for i in range(1, 2 ** len(formula.variables)):
        var_index = int(math.log2(prev_grey ^ (prev_grey := to_gray(i)))) - 1
        formula.variables[var_index].negate_value()
        if formula.value:
            return False

    return True
