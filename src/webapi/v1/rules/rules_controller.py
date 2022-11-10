from typing import List
from fastapi import APIRouter, status

from src.webapi.v1.rules.req_res_rules_models import (
    RuleResponse
)

from src.service_layer import messagebus
from src.domain.rule import Rule
from src.domain.commands import (
    RuleGetCommand,
    RuleGetAllCommand
)
from src.repositories.unit_of_work import UnitOfWork
from src.view.rule_presenter import RulePresenter

router = APIRouter()


@router.get(
    '/{rule_id}',
    status_code=status.HTTP_200_OK,
    response_model=RuleResponse
)
async def get_rule(rule_id: str):
    cmd = RuleGetCommand(rule_id)
    uow = UnitOfWork()
    rule: Rule = messagebus.handle(cmd, uow)[0]
    return RulePresenter.present(rule)


@router.get(
    '',
    status_code=status.HTTP_200_OK,
    response_model=List[RuleResponse]
)
async def get_all_rules():
    cmd = RuleGetAllCommand()
    uow = UnitOfWork()
    rules: List[Rule] = messagebus.handle(cmd, uow)[0]
    return [RulePresenter.present(rule) for rule in rules]
