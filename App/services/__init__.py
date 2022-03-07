from .health_service import health_service
from .upload_service import upload_service
from .get_images_service import get_images_service
from .pdf_tiff_to_images_service import pdf_tiff_to_images_service

services = {
    "HEALTH": health_service,
    "UPLOAD_SERVICE": upload_service,
    "GET_IMAGES_SERVICE": get_images_service,
    "PDF_TIFF_TO_IMAGES": pdf_tiff_to_images_service
}


def get_service(service, *args):
    return services.get(service)(*args)
