import os

title = "PDF/Tiff Converter"

description = '''
## You will be able to.
* **upload pdf/tiff file.**
* **obtain the images of individual pages.**
'''

version = "1.0"

openapi_tags = [
    {
        "name": "Health",
        "description": "Health check endpoint."
    },
    {
        "name": "Images",
        "description": "Get pdf/tiff pages as images."
    }
]

docs_url = "/swagger"

swagger = {
    "title": title,
    "description": description,
    "version": version,
    "docs_url": docs_url,
    "openapi_tags": openapi_tags
}

APP_DIR = os.path.join(os.getcwd(), "App/static")

PDF_TIFF_DIR = os.path.join(APP_DIR, "pdf_tiff")

IMG_DIR = os.path.join(APP_DIR, "images")
