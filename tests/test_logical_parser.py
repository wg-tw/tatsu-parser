from unittest import TestCase

from tatsu_parser.logical_operator import OperatorSpec, ExpressionSpec, LogicalOperatorParser, LogicalOperatorSemantics


class LogicalOperatorParserTest(TestCase):
    def setUp(self):
        super().setUp()

        self.parser = LogicalOperatorParser

    def test_parse_base_text(self):
        parser = self.parser()

        text1 = "and_(true, false)"
        ast1 = parser.parse(text1, rule_name="expression", semantics=LogicalOperatorSemantics())
        assert isinstance(ast1, ExpressionSpec) is True
        assert isinstance(ast1.func, OperatorSpec) is True
        assert len(ast1.func.expressions) == 2

        text2 = "and_(TRUE, False, TRUE)"
        ast2 = parser.parse(text2, rule_name="expression", semantics=LogicalOperatorSemantics())

        assert isinstance(ast2, ExpressionSpec) is True
        assert isinstance(ast2.func, OperatorSpec) is True
        assert len(ast2.func.expressions) == 3

    def test_parse_op_inside_text(self):
        text = "and_(true, true, and_(true, or_(false, true)))"

        parser = self.parser()
        ast = parser.parse(text, rule_name="expression", semantics=LogicalOperatorSemantics())

        assert ast.func.name == "and_"
        assert isinstance(ast, ExpressionSpec) is True
        assert isinstance(ast.func, OperatorSpec) is True
        assert len(ast.func.expressions) == 3
        assert ast.func.expressions[2].func.name == "and_"
        assert len(ast.func.expressions[2].func.expressions) == 2


class LogicalOperatorSpecTest(TestCase):
    def setUp(self) -> None:
        super().setUp()

        self.op_spec_cls = OperatorSpec
        self.exp_spec_cls = ExpressionSpec

    def test_func_expression_spec(self):
        expression_spec1 = self.exp_spec_cls(func=None, value="true")
        expression_spec2 = self.exp_spec_cls(func=None, value="false")
        expressions = [expression_spec1, expression_spec2]

        operator_name = "and_"
        operator_spec = self.op_spec_cls(operator_name, expressions=expressions)

        expression_spec = self.exp_spec_cls(func=operator_spec, value=None)

        assert expression_spec.func == operator_spec
        assert expression_spec.value == ""

    def test_value_expression_spec(self):
        expression_spec = self.exp_spec_cls(func=None, value="TRUE")

        assert expression_spec.func is None
        assert expression_spec.value == "true"

    def test_operator_spec(self):
        operator_name = "and_"
        expression_spec = self.exp_spec_cls(func=None, value="true")
        expressions = [expression_spec]

        operator_spec = self.op_spec_cls(operator_name, expressions=expressions)

        assert operator_spec.name == operator_name
        assert operator_spec.expressions == expressions
