import sys
import pandas as pd
import logging
from pathlib import Path

# Automatically add the project root to sys.path
project_root = Path(__file__).resolve().parent.parent
if project_root not in sys.path:
    sys.path.insert(0, str(project_root))

from db.database import DatabaseManager

def get_transformed_data( db : DatabaseManager) -> pd.DataFrame:
    """Fetches joined data with calculated fields directly from the DB."""
    query = """
        SELECT 
            (c.first_name || ' ' || c.surname) AS name, 
            o.product_name, 
            o.quantity, 
            o.price,
            (o.quantity * o.price) AS total_value
        FROM CUSTOMERS c
        JOIN ORDERS o ON c.customer_id = o.customer_id;
    """
    df = pd.read_sql_query(query, db.conn)
    
    if df.empty:
        logging.warning("No records found.")
        return None
        
    return df

def etl():

    data_path = Path(__file__).resolve().parent.parent / "data"
    db = DatabaseManager(data_path / "assessment.db")

    df = get_transformed_data(db)

    df.to_csv(data_path / "summary.csv", index=False)

etl()