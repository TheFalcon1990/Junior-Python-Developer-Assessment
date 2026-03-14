from db.database import DatabaseManager

class OrderEndpoint:
    """Handles the /order/{order_id} endpoint."""
    
    def __init__(self, db: DatabaseManager, config: dict):
        self.db = db
        self.config = config
        self.queries = self.config.get("query_templates", {})

    def get_order(self, order_id: int) -> dict:
        """Fetches order details for a specific order."""
        order_result = self.db.execute_query(self.queries.get("get_order"), (order_id,))
        
        if not order_result:
            return {"error": "Order not found"}
        
        return {
            "order": order_result[0],
        }
    
    def get_order_items(self, order_id: int) -> dict:
        """Fetches items associated with a specific order."""
        items_result = self.db.execute_query(self.queries.get("get_order_items"), (order_id,))
        
        if not items_result:
            return {"error": "No items found for this order"}
        
        return {
            "items": items_result,
        }

    def get_orders(self) -> dict:
        """Fetches all orders."""
        orders_result = self.db.execute_query(self.queries.get("select_orders"))
        return {
            "orders": orders_result
        }

    
