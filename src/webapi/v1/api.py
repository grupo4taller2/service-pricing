from fastapi import APIRouter

from src.webapi.v1 import (
    healthcheck
)

from src.webapi.v1.estimations import estimations_controller


api_router = APIRouter()

api_router.include_router(healthcheck.router,
                          prefix="/healthcheck",
                          tags=["healthcheck"])
api_router.include_router(estimations_controller.router,
                          prefix='/estimations',
                          tags=['estimations'])
