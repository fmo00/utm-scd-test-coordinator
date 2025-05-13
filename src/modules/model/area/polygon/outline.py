from pydantic import BaseModel
from typing import List

from .vertices import PolygonVertices


class PolygonOutline(BaseModel):
    vertices: List[PolygonVertices]
