from pydantic import BaseModel


class HealthSchema(BaseModel):
    message: str
