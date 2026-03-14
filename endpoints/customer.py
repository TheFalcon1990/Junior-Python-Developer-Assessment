from db.database import DatabaseManager

class CustomerEndpoint:
    """Handles the /customer/{customer_id} endpoint."""
    
    def __init__(self, db: DatabaseManager, config: dict):
        self.db = db
        self.config = config
        self.queries = self.config.get("query_templates", {})


    def get_customer(self, customer_id: int) -> dict:
        """Fetches customer profile and associated orders."""
        # Fetch customer profile
        
        profile_result = self.db.execute_query(self.queries.get("get_customer"), (customer_id,))
        
        if not profile_result:
            return {"error": "Customer not found"}
        
        return {
            "customer": profile_result[0],
        }

    def get_customer_orders(self, customer_id: int) -> dict:
        """Fetches customer profile and associated orders."""
        # Fetch customer profile
        profile_result = self.db.execute_query(self.queries.get("get_customer"), (customer_id,))
        
        if not profile_result:
            return {"error": "Customer not found"}
        
        # Fetch associated orders
        orders_result = self.db.execute_query(self.queries.get("get_customer_orders"), (customer_id,))
        
        return {
            "customer": profile_result[0],
            "orders": orders_result
        }