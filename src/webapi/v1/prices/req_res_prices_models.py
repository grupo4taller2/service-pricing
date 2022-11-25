from pydantic.main import BaseModel
from pydantic import Field


class PriceResponse(BaseModel):
    trip_id: str = Field(example='7344c4d7-451f-4abe-8435-b5dd1c191646')
    price: str = Field(example='0.0012')
