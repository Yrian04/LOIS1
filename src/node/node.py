from abc import ABC, abstractmethod


class Node(ABC):
    value_type = bool | None

    @property
    @abstractmethod
    def value(self) -> value_type: pass
