from pydantic import BaseModel
from typing import Optional


class Command(BaseModel):
    pass


class RuleGetCommand(BaseModel):
    id: Optional[str]
