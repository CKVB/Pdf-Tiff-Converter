from fastapi import status
from fastapi.responses import JSONResponse
from .clear_static_service import clear_static_service
from .. import constants as cs
from .. import config as cg
import magic


async def upload_service(file):
    file_content = await file.read()
    mime = magic.Magic(mime=True)
    file_path = f"{cs.PDF_TIFF_DIR}/{file.filename}"
    clear_static_service(cs.PDF_TIFF_DIR)
    try:
        with open(file_path, "wb") as f:
            f.write(file_content)
    except Exception as e:
        return JSONResponse(
                    content={
                        "message": f"Error occured : {e}"
                    },
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
    else:
        file_type = mime.from_file(file_path)
        if file_type in cg.SUPPORTED_FILE_TYPES.values():
            return JSONResponse(
                {
                    "message": "File Uploaded"
                },
                status_code=status.HTTP_201_CREATED
            )
        else:
            return JSONResponse(
                    {
                        "message": f"file type {file_type} not supported."
                    },
                    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
                )
