from uuid import uuid4

from src.domain.commands import (
    RuleGetCommand,
    RuleGetAllCommand,
    RuleCreateCommand,
    RuleUpdateCommand
)
from src.domain.rule import Rule
from src.service_layer.abstract_unit_of_work import AbstractUnitOfWork


def get_rule(cmd: RuleGetCommand, uow: AbstractUnitOfWork):
    with uow:
        if cmd.id:
            rule = uow.rule_repository.find_by_id(cmd.id)
        else:
            rule = uow.rule_repository.current_rule()

        uow.commit()
        return rule


def get_all_rules(cmd: RuleGetAllCommand, uow: AbstractUnitOfWork):
    with uow:
        rules = uow.rule_repository.all()
        uow.commit()
        return rules


def create_rule(cmd: RuleCreateCommand, uow: AbstractUnitOfWork):
    with uow:
        rule: Rule = Rule(
            id=str(uuid4()),
            c_km=cmd.c_km,
            c_trips_last_30m=cmd.c_trips_last_30m,
            c_rating=cmd.c_rating,
            c_min_price=cmd.c_min_price
        )
        rule = uow.rule_repository.save(rule)
        uow.commit()
        return rule


def update_rule(cmd: RuleUpdateCommand, uow: AbstractUnitOfWork):
    with uow:
        rule: Rule = uow.rule_repository.update(cmd)
        uow.commit()
        return rule
