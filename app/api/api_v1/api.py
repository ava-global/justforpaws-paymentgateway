from fastapi import APIRouter

from app.api.api_v1.endpoints import gbprime

api_router = APIRouter()
api_router.include_router(gbprime.router, prefix="/gbprime", tags=["gbprime"])
