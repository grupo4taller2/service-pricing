from __future__ import annotations
import logging
from typing import List, Dict, Callable, Type, Union
from src.domain import commands, events
from src.service_layer import handlers

from src.service_layer.abstract_unit_of_work import AbstractUnitOfWork


logger = logging.getLogger(__name__)

Message = Union[commands.Command, events.Event]


def handle(
    message: Message,
    uow: AbstractUnitOfWork,
) -> List:
    results = []
    queue = [message]
    while queue:
        message = queue.pop(0)
        if isinstance(message, events.Event):
            handle_event(message, queue, uow)
        elif isinstance(message, commands.Command):
            cmd_result = handle_command(message, queue, uow)
            results.append(cmd_result)
        else:
            raise Exception(f"{message} was not an Event or Command")
    return results


def handle_event(
    event: events.Event,
    queue: List[Message],
    uow: AbstractUnitOfWork,
):
    for handler in EVENT_HANDLERS[type(event)]:
        try:
            logger.debug("handling event %s with handler %s", event, handler)
            handler(event, uow=uow)
            queue.extend(uow.collect_new_events())
        except Exception:
            logger.exception("Exception handling event %s", event)
            continue


def handle_command(
    command: commands.Command,
    queue: List[Message],
    uow: AbstractUnitOfWork,
):
    logger.debug("handling command %s", command)
    handler = COMMAND_HANDLERS[type(command)]
    result = handler(command, uow=uow)
    queue.extend(uow.collect_new_events())
    return result


EVENT_HANDLERS = {

}  # type: Dict[Type[events.Event], List[Callable]]

COMMAND_HANDLERS = {
    commands.RuleGetCommand: handlers.get_rule,
    commands.RuleGetAllCommand: handlers.get_all_rules,
    commands.RuleCreateCommand: handlers.create_rule,
    commands.RuleUpdateCommand: handlers.update_rule,
    commands.RuleEvaluateCommand: handlers.evaluate_rule
}  # type: Dict[Type[commands.Command], Callable]
