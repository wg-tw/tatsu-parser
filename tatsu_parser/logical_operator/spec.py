from typing import Optional, List, TypeVar

from tatsu_parser.logical_operator.parser import (
    LogicalOperatorParser,
    LogicalOperatorSemantics as _LogicalOperatorSemantics,
)
from tatsu_parser.spec import Semantics, Spec

TOperatorSpec = TypeVar("TOperatorSpec", bound="OperatorSpec")


class ExpressionSpec(Spec):
    def __init__(self, func: Optional[TOperatorSpec], value: Optional[str]):
        self.func: Optional[TOperatorSpec] = func
        self.value: str = (value or "").lower()

    def __repr__(self):
        if self.func:
            return f"{self.func}"
        return self.value


class OperatorSpec(Spec):
    def __init__(self, name: str, expressions: Optional[list]):
        self.name: str = name.lower()
        self.expressions: List[ExpressionSpec] = expressions or []

    def __repr__(self):
        return f"{self.name}({self.expressions})"


class LogicalOperatorSemantics(Semantics, _LogicalOperatorSemantics):
    rule_key = "logical_operator"
    parser_cls = LogicalOperatorParser

    def expression(self, ast) -> ExpressionSpec:
        opt_spec = OperatorSpec(ast.func.name, ast.func.expressions) if ast.func else None
        return ExpressionSpec(opt_spec or ast.func, ast.value)
