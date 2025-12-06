from fastapi import APIRouter
from .schemas import EventSchemas,EventListSchems,EventCreateSchemas,EventUpdateSchemas
router = APIRouter()

@router.get("/")
def read_events() -> EventListSchems:
  return {
    "result":[{"id": 1},{"id": 2},{"id": 3},{"id": 4}] , "count":1

          }

@router.post("/")
def create_event(payload:EventCreateSchemas) -> EventSchemas:
  print(payload.page)
  data = payload.model_dump()
  return {"id": 123, **data}

@router.get("/{event_id}")
def get_event(event_id:int) -> EventSchemas:
  return{"id":event_id}

@router.put("/{event_id}")
def update_event(event_id:int,payload:EventUpdateSchemas) -> EventSchemas:
  print(payload.description)
  data = payload.model_dump()
  return {"id": event_id, **data}


