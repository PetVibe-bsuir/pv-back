from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from contextlib import asynccontextmanager
import logging
import json

from src.core import settings
from src.api import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.basicConfig(level=logging.INFO)
    openapi_schema = get_openapi(
        title="PetVibe API",
        version="SuperAlfa",
        description="Do you really need this?",
        routes=app.routes,
    )

    with open("openapi.json", "w") as f:
        json.dump(openapi_schema, f, indent=2)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(api_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
