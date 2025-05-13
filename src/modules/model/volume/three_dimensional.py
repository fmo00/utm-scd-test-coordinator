from pydantic import BaseModel
from typing import Optional

from ..area.altitude import Altitude
from ..area.circle.outline import CircleOutline
from ..area.polygon.outline import PolygonOutline


class Volume3d(BaseModel):
    outline_circle: Optional[CircleOutline] = None
    outline_polygon: Optional[PolygonOutline] = None
    altitude_lower: Altitude
    altitude_upper: Altitude
