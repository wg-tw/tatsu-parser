import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], "../parser"))


from unittest import mock, TestCase
from tatsu_parser.utils import parse


class TestParse(TestCase):
    def setUp(self):
        super().setUp()
        self.mock_parser_parse_value = "fake parse result"
        self.mock_semantics = mock.MagicMock()
        self.mock_parser = mock.MagicMock(parse=mock.MagicMock(return_value=self.mock_parser_parse_value))
        self.mock_parser_cls = mock.MagicMock(return_value=self.mock_parser)

    @mock.patch("tatsu_parser.logical_operator.LogicalOperatorSemantics")
    @mock.patch("tatsu_parser.field_selector.FieldSelectorSemantics")
    def test_parse_field_selector(self, mock_field_cls, mock_logical_cls):
        rule_key = "field_selector"

        mock_field_cls.return_value = self.mock_semantics
        mock_field_cls.rule_key = rule_key
        mock_field_cls.parser_cls = self.mock_parser_cls

        r = parse("fake text", rule_key)

        assert self.mock_parser_cls.call_count == 1
        assert self.mock_parser.parse.call_count == 1
        assert r == self.mock_parser_parse_value

    @mock.patch("tatsu_parser.logical_operator.LogicalOperatorSemantics")
    @mock.patch("tatsu_parser.field_selector.FieldSelectorSemantics")
    def test_parse_logical_operator(self, mock_field_cls, mock_logical_cls):
        rule_key = "logical_operator"

        mock_logical_cls.return_value = self.mock_semantics
        mock_logical_cls.rule_key = rule_key
        mock_logical_cls.parser_cls = self.mock_parser_cls

        r = parse("fake text", rule_key)

        assert self.mock_parser_cls.call_count == 1
        assert self.mock_parser.parse.call_count == 1
        assert r == self.mock_parser_parse_value

    def test_parse_return_none_when_given_illegal_rule_key(self):
        rule_key = "illegal rule key"

        r = parse("fake text", rule_key)
        assert r is None
