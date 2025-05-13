from pydantic import BaseModel


class CircleRadius(BaseModel):
    value: float
    units: str
