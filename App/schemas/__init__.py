from .health_schema import HealthSchema
from .upload_schema import UploadSchema
from .get_images_schema import GetImagesSchema
from .pdf_tiff_to_images_schema import PdfTiffToImagesSchema

schemas = {
    "HEALTH_SCHEMA": HealthSchema,
    "UPLOAD_SCHEMA": UploadSchema,
    "GET_IMAGES_SCHEMA": GetImagesSchema,
    "PDF_TIFF_TO_IMAGES_SCHEMA": PdfTiffToImagesSchema
}


def get_schema(schema):
    return schemas.get(schema)
