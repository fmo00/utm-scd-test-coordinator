from pydantic import BaseModel


class CircleCenter(BaseModel):
    value: float
    units: str
