from typing import Optional

from tatsu_parser.spec import Spec, Semantics
from tatsu_parser.field_selector.parser import (
    FieldSelectorParser,
    FieldSelectorSemantics as _FieldSelectorSemantics,
)


class FieldSpec(Spec):
    def __init__(self, name: str, sub_fields=Optional[list]):
        self.name: str = name
        self.sub_fields = sub_fields or []

    def __repr__(self) -> str:
        if self.sub_fields:
            return "{}({})".format(self.name, ", ".join([repr(f) for f in self.sub_fields]))
        return self.name


class FieldSelectorSemantics(Semantics, _FieldSelectorSemantics):
    rule_key = "field_selector"
    parser_cls = FieldSelectorParser

    def field_selector(self, ast):
        return ast.fields

    def field(self, ast):
        return FieldSpec(ast.name, ast.sub_fields)
