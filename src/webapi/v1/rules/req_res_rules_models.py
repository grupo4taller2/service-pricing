from pydantic.main import BaseModel
from pydantic import Field


class RuleResponse(BaseModel):
    id: str = Field(example='7344c4d7-451f-4abe-8435-b5dd1c191646')
    c_km: str = Field(example='0.0012')
    c_min_price: str = Field(example='1.15')
    c_rating: str = Field(example='3.14')
    c_trips_last_30m: str = Field(example='4.9')
