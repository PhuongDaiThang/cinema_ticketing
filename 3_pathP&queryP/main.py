from fastapi import FastAPI

app = FastAPI()

@app.get("/products/{product_id}")
def read_product(product_id: int, detail: bool = False):
    return {
        "product_id": product_id,
        "detail": detail
    }

@app.get("/orders/{order_id}/items")
def read_order_items(order_id: int, status: str = "pending"):
    return {
        "order_id": order_id,
        "status_filter": status
    }
