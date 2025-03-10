from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from database import fetch_all_items, create_item

app = FastAPI()

# Dummy in-memory database simulation
items_db = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Example Application!"}

@app.get("/items/", response_model=List[dict])
def read_items():
    """
    Fetch all items from the in-memory database.
    """
    return fetch_all_items()

@app.post("/items/", status_code=201)
def add_item(item: dict):
    """
    Add a new item to the in-memory database.
    """
    create_item(item)
    return {"message": "Item added successfully", "item": item}
