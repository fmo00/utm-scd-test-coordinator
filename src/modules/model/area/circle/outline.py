from pydantic import BaseModel

from .center import CircleCenter
from .radius import CircleRadius


class CircleOutline(BaseModel):
    center: CircleCenter
    radius: CircleRadius
