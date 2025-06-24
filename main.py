from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

fake_items_db = {}

# Pydantic model for item
class Item(BaseModel):
    name: str
    price: float
    description: str = None  # Optional field

# GET Method
@app.get("/")
def read_root():
    return {"message": "The app is starting"}

# GET with path and query parameters
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

# POST Method
@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    fake_items_db[item_id] = item
    return {"message": "Item created", "item_id": item_id, "data": item}

# DELETE: Delete an item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id in fake_items_db:
        del fake_items_db[item_id]
        return {"message": f"Item {item_id} deleted"}
    return {"error": f"Item {item_id} not found"}