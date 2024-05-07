import unittest

from src.logical_formula.logical_formula_lexer import LogicalFormulaLexer
from src.logical_formula.token import Token


class TestLogicalFormulaLexer(unittest.TestCase):
    def setUp(self):
        self.lexer = LogicalFormulaLexer()

    def test_analyze(self):
        tokens = self.lexer.analyze(r"((!(A/\B))\/((0->B)~1))")
        self.assertEqual(tokens, [
            Token.left_bracket,
            Token.left_bracket,
            Token.negation,
            Token.left_bracket,
            'A',
            Token.conjunction,
            'B',
            Token.right_bracket,
            Token.right_bracket,
            Token.disjunction,
            Token.left_bracket,
            Token.left_bracket,
            Token.false,
            Token.implication,
            'B',
            Token.right_bracket,
            Token.equivalence,
            Token.true,
            Token.right_bracket,
            Token.right_bracket,
        ])

    def test_analyse_unknown_lex(self):
        self.assertRaises(
            ValueError,
            self.lexer.analyze,
            r"((!(A\B))\/((0->D)~1))"
        )
