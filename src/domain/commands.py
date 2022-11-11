from pydantic import BaseModel
from typing import Optional


class Command(BaseModel):
    pass


class RuleGetCommand(Command):
    id: Optional[str]


class RuleGetAllCommand(Command):
    pass


class RuleCreateCommand(Command):
    c_km: str
    c_trips_last_30m: str
    c_rating: str
    c_min_price: str


class RuleUpdateCommand(RuleCreateCommand):
    id: str
    c_km: Optional[str]
    c_trips_last_30m: Optional[str]
    c_rating: Optional[str]
    c_min_price: Optional[str]
