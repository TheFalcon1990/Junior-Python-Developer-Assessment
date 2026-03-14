from fastapi import FastAPI, HTTPException
import uvicorn
from pathlib import Path
import json
from db.database import DatabaseManager
from endpoints.customer import CustomerEndpoint
from endpoints.order import OrderEndpoint

app = FastAPI(title="Customer Information API")

# Initialize database and endpoints

DATA = Path(__file__).resolve().parent / 'data'
DB = DatabaseManager(DATA / 'assessment.db')

CONFIG_PATH = Path(__file__).resolve().parent / "config" / "config.json"
config = json.load(open(CONFIG_PATH))

customer_endpoint = CustomerEndpoint(DB, config)
order_endpoint = OrderEndpoint(DB, config)

@app.get("/customer/{customer_id}")
def get_customer(customer_id: int):
    """
    Returns a combined object containing profile details 
    and all associated orders for a specific customer.
    """
    result = customer_endpoint.get_customer_orders(customer_id)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result

@app.get("/orders")
def get_orders():
    """
    Returns list of all orders.
    """
    return order_endpoint.get_orders()

@app.get("/order/{order_id}")
def get_order(order_id: int):
    """
    Returns details of a specific order.
    """
    result = order_endpoint.get_order(order_id)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result

if __name__ == "__main__":
    
    print("🚀 API starting... View docs at http://127.0.0.1:8000/docs")
    uvicorn.run(app, host="127.0.0.1", port=8000)