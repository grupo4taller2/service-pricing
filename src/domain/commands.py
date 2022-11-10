from pydantic import BaseModel
from typing import Optional


class Command(BaseModel):
    pass


class RuleGetCommand(Command):
    id: Optional[str]


class RuleGetAllCommand(Command):
    pass
