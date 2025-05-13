from pydantic import BaseModel


class Altitude(BaseModel):
    value: float
    reference: str
    units: str
