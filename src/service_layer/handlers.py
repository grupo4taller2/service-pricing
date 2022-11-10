from src.domain.commands import (
    RuleGetCommand,
    RuleGetAllCommand
)
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
