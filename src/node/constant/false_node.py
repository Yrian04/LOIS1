from .constant_node import ConstantNode
from src.singleton import singleton


@singleton
class FalseNode(ConstantNode):
    VALUE = False
