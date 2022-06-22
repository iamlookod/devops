from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Item(BaseModel):
    id: Optional[int]
    name: str


items = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
    {"id": 3, "name": "Item 3"},
]


@app.get("/")
def get_items():
    return items


@app.get("/{item_id}")
def get_item(item_id: int):
    result = [item for item in items if item["id"] == item_id]
    return result


@app.post("/")
def create_item(item: Item):
    id = max([item['id'] for item in items]) + 1
    new_item = {'id': id, 'name': item.name}
    items.append(new_item)
    return new_item


@ app.put("/{item_id}")
def update_item(item_id: int, item: Item):
    update_item = {
        "id": item_id,
        "name": item.name
    }
    item_list = [item for item in items if item["id"] == item_id]
    if len(item_list) > 0:
        items.remove(item_list[0])
        items.append(update_item)
        return item
    else:
        return HTTPException(status_code=404, detail="Item not found")


@ app.delete("/{item_id}")
def delete_item(item_id: int):
    item_list = [item for item in items if item["id"] == item_id]
    if len(item_list) > 0:
        items.remove(item_list[0])
        return bool(True)
    else:
        return HTTPException(status_code=404, detail="Item not found")
