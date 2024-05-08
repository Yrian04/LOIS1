# Выполнили студенты группы 221701 БГУИР:
# - Глёза Егор Дмитриевич
# - Крупский Артём Викторович
#
# Класс лексера логических выражений
# 08.05.2024
#
# Источники:
# - Проектирование программного обеспечения интеллектуальных систем (3 семестр)
#

from .token import Token


class LogicalFormulaLexer:
    prefix_lex_cutters = {
        Token.disjunction: lambda x: x.removeprefix('\\/'),
        Token.conjunction: lambda x: x.removeprefix('/\\'),
        Token.implication: lambda x: x.removeprefix('->'),
        Token.equivalence: lambda x: x.removeprefix('~'),
        Token.negation: lambda x: x.removeprefix('!'),
        Token.left_bracket: lambda x: x.removeprefix('('),
        Token.right_bracket: lambda x: x.removeprefix(')'),
        Token.true: lambda x: x.removeprefix('1'),
        Token.false: lambda x: x.removeprefix('0')
    }

    def analyze(self, string: str) -> list[Token | str]:
        tokens = []
        while string:
            new_string = self._variable_cutter(tokens, string)
            for token_type in self.prefix_lex_cutters:
                string_without_lex = self.prefix_lex_cutters[token_type](new_string)
                if string_without_lex != new_string:
                    tokens.append(token_type)
                    new_string = string_without_lex
            if new_string == string:
                raise ValueError(f"Unknown lex at {len(tokens)+1} position")
            string = new_string
        return tokens

    def _variable_cutter(self, tokens: list[Token | str], string: str) -> str:
        if string[0].isupper():
            tokens.append(string[0])
            return string[1:]
        return string
