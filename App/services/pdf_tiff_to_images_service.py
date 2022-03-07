from .. import constants as cs
from .. import config as cg
from .split_pdf_service import split_pdf_service
from .split_tiff_service import split_tiff_service
from .clear_static_service import clear_static_service
import os
import magic


def pdf_tiff_to_images_service():
    file = os.path.join(cs.PDF_TIFF_DIR, os.listdir(cs.PDF_TIFF_DIR)[0])
    
    clear_static_service(cs.IMG_DIR)

    mime = magic.Magic(mime=True)
    file_type = mime.from_file(file)

    if file_type == cg.SUPPORTED_FILE_TYPES.get("PDF"):
        return split_pdf_service(file)
    elif file_type == cg.SUPPORTED_FILE_TYPES.get("TIFF"):
        return split_tiff_service(file)
