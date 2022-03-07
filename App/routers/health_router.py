from fastapi import APIRouter
from ..services import get_service
from .. import config as c

health_router = APIRouter()


@health_router.get("/health", responses=c.health_response)
def health():
    return get_service("HEALTH")
