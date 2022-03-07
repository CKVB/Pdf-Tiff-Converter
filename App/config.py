from pydantic import BaseSettings
from typing import List
from .constants import swagger
from fastapi import status
from .schemas import get_schema


class SwaggerConfig(BaseSettings):
    title: str
    description: str
    version: str
    docs_url: str
    openapi_tags: List[dict]


swagger_config = SwaggerConfig(**swagger)


SUPPORTED_FILE_TYPES = {"PDF": "application/pdf", "TIFF": "image/tiff"}


health_response = {
    status.HTTP_200_OK: {
        "model": get_schema("HEALTH_SCHEMA")
    }
}

upload_file_response = {
    status.HTTP_201_CREATED: {
        "model": get_schema("UPLOAD_SCHEMA")
    }, 
    status.HTTP_422_UNPROCESSABLE_ENTITY: {
        "model": get_schema("UPLOAD_SCHEMA")
    }    
}

pdf_tiff_to_images_response = {
    status.HTTP_200_OK: {
        "model": get_schema("PDF_TIFF_TO_IMAGES_SCHEMA")
    },
    status.HTTP_500_INTERNAL_SERVER_ERROR: {
        "model": get_schema("PDF_TIFF_TO_IMAGES_SCHEMA")
    }    
}

get_images_response = {
    status.HTTP_200_OK: {
        "model": get_schema("GET_IMAGES_SCHEMA")
    },
    status.HTTP_404_NOT_FOUND: {
        "model": get_schema("GET_IMAGES_SCHEMA")
    }
}
