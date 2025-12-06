from pydantic import BaseModel
from typing import List, Optional

class EventCreateSchemas(BaseModel): # {"id": 12}
  page: str

class EventUpdateSchemas(BaseModel): # {"id": 12}
  description: str

class EventSchemas(BaseModel): # {"id": 12}
  id: int
  page: Optional[str] = ""
  description: Optional[str] = ""

class EventListSchems(BaseModel): # {"id": 12}
  result : List[EventSchemas]
  count : int

