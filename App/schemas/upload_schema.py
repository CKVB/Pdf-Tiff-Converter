from pydantic import BaseModel


class UploadSchema(BaseModel):
    message: str
