from pathlib import Path
import json
from database import DatabaseManager
from db_tables import TableManager
from db_data_generator import DataGenerator


def main():
    # Load config
    config_path = Path(__file__).resolve().parent.parent / "config" / "config.json"
    with open(config_path, 'r') as f:
        config = json.load(f)

    # Initialize database manager
    data_path = Path(__file__).resolve().parent.parent / "data"

    if not data_path.exists():
        data_path.mkdir(parents=True)

    db = DatabaseManager(data_path / "assessment.db")

    print("Database initialized at:", data_path / "assessment.db")
    # Setup tables
    table_manager = TableManager(db, config)
    table_manager.setup_tables()

    print("Tables created successfully.")
    # Generate and insert data
    generator = DataGenerator(db, config)
    generator.generate_and_insert()

    print("Data inserted successfully.")
    db.close()

main()