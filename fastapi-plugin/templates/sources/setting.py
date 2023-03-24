from pydantic import BaseSettings

import os


class Setting(BaseSettings):
    APPLICATION_DEBUG: bool = os.getenv(key="APPLICATION_DEBUG")
    APPLICATION_DESCRIPTION: str = "{{project_description}}"
    APPLICATION_NAME: str = "{{project_name}}"
    APPLICATION_TITLE: str = "{{project_title}}"
    APPLICATION_VERSION: str = "{{project_version}}"

    API_PREFIX_V1: str = "/v1"

    SERVER_HOST: str = os.getenv(key="SERVER_HOST")
    SERVER_PORT: int = os.getenv(key="SERVER_PORT")

    class Config:
        env_file = ".env"

    @property
    def application_properties(self):
        return {
            "debug": self.APPLICATION_DEBUG,
            "description": self.APPLICATION_DESCRIPTION,
            "docs_url": f"{self.API_PREFIX_V1}/documentation/swagger",
            "openapi_url": f"{self.API_PREFIX_V1}/documentation/openapi.json",
            "redoc_url": f"{self.API_PREFIX_V1}/documentation/redoc",
            "title": self.APPLICATION_TITLE,
            "version": self.APPLICATION_VERSION,
        }


setting = Setting()
