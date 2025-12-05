from fastapi import APIRouter
from .schemas import EventSchems
router = APIRouter()

@router.get("/")
def read_items():
  return {"items":[1,2,3,4]}

@router.get("/{event_id}")
def get_items(event_id:int) -> EventSchems:
  return {"id":event_id}
