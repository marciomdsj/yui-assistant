from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from typing import Dict, Any, Optional, List

class SystemContext(BaseModel):
    now_utc: datetime
