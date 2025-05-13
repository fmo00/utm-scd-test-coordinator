from pydantic import BaseModel


class PolygonVertices(BaseModel):
    lng: float
    lat: float
