from fastapi.responses import JSONResponse
from fastapi import status


def health_service():
    content = {
        "message": "running",
    }
    return JSONResponse(content=content, status_code=status.HTTP_200_OK)
