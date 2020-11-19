from typing import Type

from tatsu.parsing import Parser  # type: ignore


class Semantics:
    rule_key = ""
    parser_cls: Type[Parser] = Parser


class Spec:
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__
