from PIL import Image
from .. import constants as cs
from fastapi.responses import JSONResponse
from fastapi import status
import os


def split_tiff_service(file):
    try:
        tiff_file = Image.open(file)
        tiff_file_name = os.path.basename(file).split(".")[0]
        for index in range(tiff_file.n_frames):
            tiff_file.seek(index)
            tiff_file_path = os.path.join(cs.IMG_DIR, f"{tiff_file_name}-{index}.jpg")
            tiff_file.save(tiff_file_path, "JPEG")
    except Exception as e:
        return JSONResponse(
                content={
                    "message": str(e) 
                },
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    else:
        return JSONResponse(
                content={
                    "message": "success"
                },
                status_code=status.HTTP_200_OK
            )
