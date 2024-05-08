from ..nonconstant_node import OperationNode, Node, NonConstantNode


class NegationNode(OperationNode):
    def __init__(self):
        super().__init__()
        self._negated_node: Node | None = None

    @property
    def negated_node(self):
        return self._negated_node

    @negated_node.setter
    def negated_node(self, value):
        if isinstance(self._negated_node, NonConstantNode):
            self._negated_node._remove_parent(self)

        self._negated_node = value

        if isinstance(self._negated_node, NonConstantNode):
            self._negated_node._add_parent(self)

        self.calculate_value()
        self._on_value_changed()

    def calculate_value(self) -> None:
        self._value = not self._negated_node.value
