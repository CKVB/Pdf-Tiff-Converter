from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .config import swagger_config as swg
from .routers import get_router
from . import constants as cs


def create_app():
    app = FastAPI(
            title=swg.title,
            description=swg.description,
            version=swg.version,
            openapi_tags=swg.openapi_tags,
            docs_url=swg.docs_url
        )
    app.mount("/static", StaticFiles(directory=cs.IMG_DIR), name="static")
    app.include_router(get_router("HEALTH_ROUTER"), tags=["Health"])
    app.include_router(get_router("APP_ROUTER"), tags=["Images"])
    return app
