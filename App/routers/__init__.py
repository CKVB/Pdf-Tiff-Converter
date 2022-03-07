from .health_router import health_router
from .app_router import app_router

routers = {
    "HEALTH_ROUTER": health_router,
    "APP_ROUTER": app_router
}


def get_router(router):
    return routers.get(router)
