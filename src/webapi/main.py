from fastapi import FastAPI, APIRouter
from src.conf.config import Settings
from src.webapi.v1 import api


root_router = APIRouter()
app = FastAPI(title="Pricing API", openapi_url="/openapi.json")

app.include_router(api.api_router, prefix=Settings().API_V1_STR)
app.include_router(root_router)
