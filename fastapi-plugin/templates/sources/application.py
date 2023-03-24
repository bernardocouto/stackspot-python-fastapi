from fastapi import FastAPI
from sources.controllers.router import router
from sources.setting import setting


def create_application():
    application = FastAPI(**setting.application_properties)
    application.include_router(prefix=setting.API_PREFIX_V1, router=router)
    return application
