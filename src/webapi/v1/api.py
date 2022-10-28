from fastapi import APIRouter

from src.webapi.v1 import (
    healthcheck
)


api_router = APIRouter()

api_router.include_router(healthcheck.router,
                          prefix="/healthcheck",
                          tags=["healthcheck"])
