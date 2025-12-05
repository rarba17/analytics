from typing import Union
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get('/')
async def read_root():
    return {"message": "Welcome to the FastAPI application!"}

@app.get('/items/{item_id}')
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/healthz")
async def read_api_health():
    return {"status":"ok"}