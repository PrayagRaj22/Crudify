from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

route = APIRouter(prefix="/items")

# Fake DB
items = []


# Schema
class Item(BaseModel):
    id: int
    name: str
    price: float


# CREATE
@route.post("/")
def create_item(item: Item):
    items.append(item)
    return item


# READ ALL
@route.get("/")
def get_items():
    return items


# READ ONE
@route.get("/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


# UPDATE
@route.put("/{item_id}")
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items):
        if item.id == item_id:
            items[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")


# DELETE
@route.delete("/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item.id == item_id:
            items.pop(index)
            return {"message": "Deleted"}
    raise HTTPException(status_code=404, detail="Item not found")
