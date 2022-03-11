from .. import constants as cs
from fastapi.responses import JSONResponse
from fastapi import status
import subprocess
import os


def split_pdf_service(file):
    file_name = os.path.basename(file).split(".")[0]
    command = [
        "pdftoppm",
        "-jpeg",
        file,
        os.path.join(cs.IMG_DIR, file_name)
    ]
    try:
        subprocess.check_output(command, timeout=1000)
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
