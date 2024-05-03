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
