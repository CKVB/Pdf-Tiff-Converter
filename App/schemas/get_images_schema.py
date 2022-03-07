from pydantic import BaseModel
from typing import List


class GetImagesSchema(BaseModel):
    count: int
    images: List[str]
