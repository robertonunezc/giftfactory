from fastapi import FastAPI
from fastapi.routing import APIRoute
from api.main import api_router
from core.config import settings

app = FastAPI(
    title="GiftFactory API",
)

app.include_router(api_router, prefix=settings.API_V1_STR)