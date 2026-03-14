import json
from pathlib import Path
from database import DatabaseManager

class TableManager:
    """Handles table creation using configuration."""

    def __init__(self, db: DatabaseManager, config: dict):
        self.db = db
        self.config = config

    def setup_tables(self):
        """Creates tables dynamically based on the config file."""
        for table_name, columns in self.config['database'].items():
            print(f"Setting up table: {table_name}")
            column_definitions = ", ".join([f"{col} {definition}" for col, definition in columns.items()])
            create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions})"
            print(f"Executing query: {create_table_query}")
            self.db.execute_query(create_table_query)