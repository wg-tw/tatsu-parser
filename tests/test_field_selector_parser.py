from unittest import TestCase

from tatsu_parser.field_selector import FieldSelectorParser, FieldSelectorSemantics, FieldSpec


class FieldSelectorParserTest(TestCase):
    def setUp(self):
        super().setUp()

        self.parser_cls = FieldSelectorParser
        self.rule_key = "field_selector"
        self.semantics_cls = FieldSelectorSemantics

    def test_parse_base_text(self):
        parser = self.parser_cls()

        text = "id,name,user_no"

        ast = parser.parse(text, rule_name=self.rule_key, semantics=self.semantics_cls())

        assert str(ast) == "[id, name, user_no]"
        assert isinstance(ast[0], FieldSpec) is True

    def test_parse_sub_fields_text(self):
        parser = self.parser_cls()

        text = "id,name,user(id,name)"

        ast = parser.parse(text, rule_name=self.rule_key, semantics=self.semantics_cls())

        assert str(ast) == "[id, name, user(id, name)]"
        assert isinstance(ast[2], FieldSpec) is True
        assert len(ast[2].sub_fields) == 2


class FieldSelectorSpecTest(TestCase):
    def setUp(self) -> None:
        super().setUp()

        self.field_spec_cls = FieldSpec

    def test_field_spec(self):
        sub_fields = [self.field_spec_cls(name="id"), self.field_spec_cls(name="name")]

        field_spec = self.field_spec_cls(name="user", sub_fields=sub_fields)

        assert field_spec.name == "user"
        assert field_spec.sub_fields == sub_fields
