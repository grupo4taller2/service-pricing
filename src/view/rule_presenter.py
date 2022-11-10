from src.domain.rule import Rule
from src.webapi.v1.rules.req_res_rules_models import RuleResponse


class RulePresenter:

    @classmethod
    def present(cls, rule: Rule):
        return RuleResponse(
            c_km=str(rule.c_km),
            c_min_price=str(rule.c_min),
            c_rating=str(rule.c_rating),
            c_trips_last_30m=str(rule.c_trips_last_30m),
        )
