from .nonconstant_node import NonConstantNode


class VariableNode(NonConstantNode):
    @NonConstantNode.value.setter
    def value(self, value: NonConstantNode.value_type):
        self._value = value
        self._on_value_changed()
