from fastapi import APIRouter, status

from src.webapi.v1.prices.req_res_prices_models import PriceResponse
from src.service_layer import messagebus
from src.domain.commands import (
    FinishedTripPriceCommand,
)
from src.repositories.unit_of_work import UnitOfWork

router = APIRouter()


@router.get(
    '/{trip_id}',
    status_code=status.HTTP_200_OK,
    response_model=PriceResponse
)
async def get_price(trip_id: str):
    cmd = FinishedTripPriceCommand(trip_id=trip_id)
    uow = UnitOfWork()
    price = messagebus.handle(cmd, uow)[0]
    return PriceResponse(trip_id=trip_id, price=price)
