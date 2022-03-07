from fastapi import APIRouter, File, UploadFile, status, Request
from .. import config as cg
from ..services import get_service

app_router = APIRouter()


@app_router.post("/upload", status_code=status.HTTP_201_CREATED, responses=cg.upload_file_response)
async def create_upload_file(file: UploadFile = File(...)):
    return await get_service("UPLOAD_SERVICE", file)


@app_router.get("/convert", responses=cg.pdf_tiff_to_images_response)
def convert_pdf_tiff_to_images():
    return get_service("PDF_TIFF_TO_IMAGES")


@app_router.get("/images", responses=cg.get_images_response)
def get_pdf_tiff_images(request: Request):
    return get_service("GET_IMAGES_SERVICE", str(request.url).split("images")[0])
