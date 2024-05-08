# Выполнили студенты группы 221701 БГУИР:
# - Глёза Егор Дмитриевич
# - Крупский Артём Викторович
#
# Класс парсера логических выражений
# 08.05.2024
#
# Источники:
# - Проектирование программного обеспечения интеллектуальных систем (3 семестр)
#

from ..node import Node
from ..node.nonconstant import operations
from ..node.nonconstant.variable_node import VariableNode as Variable
from ..node.constant.false_node import FalseNode
from ..node.constant.true_node import TrueNode
from .token import Token


def standard_validator(variable_name: str) -> str:
    if len(variable_name) != 1:
        raise ValueError("Variable name must be 1 length")
    if not variable_name.isupper():
        raise ValueError("Variable name must be upper letter")
    return variable_name


class LogicalFormulaParser:
    operations_types = {
        Token.conjunction: operations.ConjunctionNode,
        Token.disjunction: operations.DisjunctionNode,
        Token.implication: operations.ImplicationNode,
        Token.equivalence: operations.EquivalenceNode,
    }

    __vars = {}

    def __init__(self, var_name_validator=standard_validator):
        self._var_name_validator = var_name_validator

    def parse(self, tokens: list[Token]) -> Node:
        self.__vars = {}
        return self._build_tree(tokens)

    def _build_tree(self, tokens: list[Token]) -> Node:
        match tokens:
            case (Token.left_bracket,
                  Token.negation,
                  *subformula,
                  Token.right_bracket):
                negation = operations.NegationNode()
                negation.negated_node = self._build_tree(subformula)
                return negation
            case [str()] as var_list:
                var = var_list[0]
                if self._var_name_validator(var) not in self.__vars:
                    self.__vars[var] = Variable()
                return self.__vars[var]
            case [Token.false]:
                return FalseNode()
            case [Token.true]:
                return TrueNode()

        left_subformula, operation, right_subformula = self.__pick_out_binary_relation(tokens)

        root = self.operations_types[operation]()
        root.left = self._build_tree(left_subformula)
        root.right = self._build_tree(right_subformula)

        return root

    @classmethod
    def __pick_out_binary_relation(cls, tokens: list[Token]):
        if tokens[0] != Token.left_bracket:
            raise ValueError("No start bracket")

        match tokens:
            case (Token.left_bracket,
                  str() | Token.false | Token.true as arg1,
                  Token.equivalence |
                  Token.conjunction |
                  Token.disjunction |
                  Token.implication as operation,
                  str() | Token.false | Token.true as arg2,
                  Token.right_bracket):
                return [arg1], operation, [arg2]

            case (Token.left_bracket,
                  *subformula,
                  Token.equivalence |
                  Token.conjunction |
                  Token.disjunction |
                  Token.implication as operation,
                  str() | Token.false | Token.true as arg2,
                  Token.right_bracket):
                return subformula, operation, [arg2]

            case (Token.left_bracket,
                  str() | Token.false | Token.true as arg1,
                  Token.equivalence |
                  Token.conjunction |
                  Token.disjunction |
                  Token.implication as operation,
                  *subformula,
                  Token.right_bracket):
                return [arg1], operation, subformula

        brackets = 0

        left_subformula = []
        operation = None
        right_subformula = []

        for token in tokens[1:-1]:
            if token == Token.left_bracket:
                brackets += 1
            elif token == Token.right_bracket:
                brackets -= 1

            if brackets > 0:
                ValueError("Invalid brackets")

            if not operation:
                if brackets == 0 and token in cls.operations_types:
                    operation = token
                    continue
                left_subformula.append(token)
            else:
                right_subformula.append(token)

        if brackets != 0:
            raise ValueError("Unclose bracket")

        if not left_subformula:
            raise ValueError("No left operand")

        if not right_subformula:
            raise ValueError("No right operand")

        return left_subformula, operation, right_subformula
