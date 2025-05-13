from pydantic import BaseModel

from . import TimeValue
from .three_dimensional import Volume3d


class Volume4d(BaseModel):
    volume: Volume3d
    time_start: TimeValue
    time_end: TimeValue
