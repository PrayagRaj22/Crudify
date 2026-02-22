from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from routers import api_routes

app = FastAPI()

# Fake DB
items = []


# Schema
class Item(BaseModel):
    id: int
    name: str
    price: float


# Include router from sub-module
app.include_router(api_routes)


# CREATE
@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return item


# READ ALL
@app.get("/items")
def get_items():
    return items


# READ ONE
@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


# UPDATE
@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items):
        if item.id == item_id:
            items[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")


# DELETE
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item.id == item_id:
            items.pop(index)
            return {"message": "Deleted"}
    raise HTTPException(status_code=404, detail="Item not found")
