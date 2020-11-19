from typing import Type, Optional, Dict

from tatsu_parser.spec import Semantics


def parse(text: str, rule_key) -> Optional[Semantics]:
    from tatsu_parser.field_selector import FieldSelectorSemantics
    from tatsu_parser.logical_operator import LogicalOperatorSemantics

    semantics_map: Dict[str, Type[Semantics]] = {
        "field_selector": FieldSelectorSemantics,
        "logical_operator": LogicalOperatorSemantics,
    }

    semantics_cls = semantics_map.get(rule_key)
    if not semantics_cls:
        return None

    parser = semantics_cls.parser_cls()
    return parser.parse(text, rule_name=semantics_cls.rule_key, semantics=semantics_cls())
