from pydantic import BaseModel
from typing import Optional

from . import Volume4d


class OirDetails(BaseModel):
    volumes: Optional[Volume4d] = None
    off_nominal_volumes: Optional[Volume4d] = None
    priority: Optional[int] = None
