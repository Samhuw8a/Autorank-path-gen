import yaml
from abc import ABC, abstractmethod
from typing import Any


class Writer:
    def __init__(self, *ranks: Any) -> None:
        pass

    def write_yaml(self, file: str) -> None:
        return NotImplemented
