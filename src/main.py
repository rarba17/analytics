from typing import Union
from fastapi import FastAPI, HTTPException
from api.events.routing import router as event_router

app = FastAPI()
app.include_router(event_router, prefix='/api/events')

@app.get('/')
async def read_root():
    return {"message": "Welcome to the FastAPI application!"}

@app.get('/items/{item_id}')
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/healthz")
async def read_api_health():
    return {"status":"ok"}