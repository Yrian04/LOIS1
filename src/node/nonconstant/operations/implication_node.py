from ..nonconstant_node import OperationNode


class ImplicationNode(OperationNode):
    def _operation(self, right_value: OperationNode.value_type,
                   left_value: OperationNode.value_type) -> OperationNode.value_type:
        return right_value <= left_value
