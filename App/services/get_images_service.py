from .. import constants as cs
from fastapi.responses import JSONResponse
from fastapi import status
import os


def get_images_service(host):
    images = [os.path.join(host, f"static/{image}") for image in os.listdir(cs.IMG_DIR)]
    content = {
            "count": len(images),
            "images": images
        }
    if images:
        return JSONResponse(
                content=content,
                status_code=status.HTTP_200_OK
            )
    else:
        return JSONResponse(
                content=content,
                status_code=status.HTTP_404_NOT_FOUND
            )
