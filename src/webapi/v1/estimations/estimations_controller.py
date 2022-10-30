from fastapi import APIRouter, status

from src.webapi.v1.estimations.req_res_estimations_models import (
    EstimationResponse
)

router = APIRouter()


@router.get(
    '',
    status_code=status.HTTP_200_OK,
    response_model=EstimationResponse
)
async def estimate_trip(
        rider_username: str = '',
        origin_address: str = '',
        origin_latitude: float = -9000.9,
        origin_longitude: float = -9000.9,
        destination_address: str = '',
        destination_latitude: float = -9000.9,
        destination_longitude: float = -9000.9,
        estimated_time: int = 0,
        distance: int = 0):

    return EstimationResponse(
        estimated_price=0.000013*distance
    )
