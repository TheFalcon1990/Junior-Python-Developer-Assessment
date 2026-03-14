import sqlite3
from pathlib import Path

class DatabaseManager:
    """Handles SQLite connection and generic database operations."""

    def __init__(self, db_path: Path):
        """Initializes the connection to the SQLite database."""
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row  # Enable row-as-dictionary behavior
        self.cursor = self.conn.cursor()

    def execute_query(self, query: str, params: tuple = None):
        """
        Executes a SQL query with optional parameters.

        Args:
            query (str): The SQL query to execute.
            params (tuple): Optional parameters for the query.

        Returns:
            list: A list of rows (as dictionaries) returned by the query.
        """
        try:
            self.cursor.execute(query, params or ())
            self.conn.commit()
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []

    def insert_data(self, table_name: str, data: list):
        """Inserts a list of dictionaries into the specified table."""
        if not data:
            return

        keys = data[0].keys()
        columns = ", ".join(keys)
        placeholders = ", ".join(["?"] * len(keys))
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

        values = [tuple(item.values()) for item in data]
        self.cursor.executemany(sql, values)
        self.conn.commit()

    def close(self):
        """Closes the database connection."""
        self.conn.close()