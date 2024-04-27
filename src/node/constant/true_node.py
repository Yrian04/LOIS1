from .constant_node import ConstantNode
from src.singleton import singleton


@singleton
class TrueNode(ConstantNode):
    VALUE = True
