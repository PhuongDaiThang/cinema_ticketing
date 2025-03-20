from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Định nghĩa request body model
class Item(BaseModel):
    name: str
    price: float
    quantity: int

# Nhận dữ liệu từ request body (POST)
@app.post("/items/")
def create_item(item: Item):
    total = item.price * item.quantity
    return {"item": item.name, "total_price": total}
