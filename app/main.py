from fastapi import FastAPI, HTTPException
from app.order import Order


orders: list[Order] = [
    Order(0, 'First user', 'First desc', [0,1,2]),
    Order(1, 'Second user', 'Second desc', [3]),
    Order(2, 'Third user', 'Third desc', [0,2]),
    Order(3, 'Forth user', 'Forth desc', [0,1,3]),
    Order(4, 'Fifth user', 'Forth desc', [2,3])
]

app = FastAPI()


@app.get("/v1/orders")
async def get_orders():
    return orders

@app.get("/v1/orders/{id}")
async def get_menu_item_by_id(id: int):
    result = [item for item in orders if item.id == id]
    if len(result) > 0:
        return result[0]
    raise HTTPException(status_code=404, detail="Order not found")

@app.get("/__health")
async def check_service():
    return 