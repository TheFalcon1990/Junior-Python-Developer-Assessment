# Junior Data Engineer Assessment

A Python-based data processing and API system that demonstrates database management, synthetic data generation, REST API development, and ETL processes. This project creates a customer-order database, generates sample data, provides API endpoints for data retrieval, and performs data transformation to generate summary reports.

## Features

- **Database Management**: SQLite-based customer and order database with configurable schema
- **Synthetic Data Generation**: Automated creation of realistic customer and order data using Faker
- **REST API**: FastAPI-based endpoints for customer and order information retrieval
- **ETL Processing**: Data transformation pipeline that generates customer spending summaries
- **Configurable Architecture**: JSON-based configuration for database schema and queries

## Prerequisites

- Python 3.8 or higher
- Virtual environment (recommended)

## Installation

1. **Clone or download the project**
   ```bash
   cd path/to/project
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### 1. Database Setup

Build the database with tables and sample data:
```bash
python db/main.py
```
This creates `assessment.db` in the `data/` folder with 50 customers and their associated orders.

### 2. Start the API Server

Launch the FastAPI server:
```bash
python api.py
```
The API will be available at `http://127.0.0.1:8000`

#### API Endpoints

- `GET /customer/{customer_id}` - Get customer profile with all associated orders
- `GET /order/{order_id}` - Get details of a specific order

#### Example API Usage

```bash
# Get customer with ID 2 and their orders
curl http://127.0.0.1:8000/customer/2

# Get specific order
curl http://127.0.0.1:8000/order/1
```

### 3. Run ETL Process

Generate customer spending summary:
```bash
python process/etl_customer_totals.py
```
This creates `summary.csv` in the `data/` folder with customer names, products, quantities, prices, and calculated total values.

## Project Structure

```
├── api.py                    # Main FastAPI application
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── config/
│   └── config.json          # Database schema and query templates
├── data/
│   ├── assessment.db        # SQLite database (generated)
│   └── summary.csv          # ETL output (generated)
├── db/
│   ├── __init__.py
│   ├── database.py          # Database connection manager
│   ├── db_tables.py         # Dynamic table creation from config
│   ├── db_data_generator.py # Synthetic data generation
│   └── main.py              # Database setup script
├── endpoints/
│   ├── customer.py          # Customer API endpoint logic
│   └── order.py             # Order API endpoint logic
└── process/
    └── etl_customer_totals.py # ETL pipeline for data transformation
```

## Configuration

The `config/config.json` file contains:

- **Database Schema**: Table definitions for CUSTOMERS and ORDERS tables
- **Data Generation**: Row count configuration (default: 50 customers)
- **Query Templates**: Predefined SQL queries for API endpoints

### Database Schema

**CUSTOMERS Table:**
- `customer_id` (INTEGER PRIMARY KEY)
- `first_name` (VARCHAR)
- `surname` (VARCHAR)
- `email` (VARCHAR)
- `status` (VARCHAR: active/archived/suspended)

**ORDERS Table:**
- `order_id` (INTEGER PRIMARY KEY)
- `customer_id` (INTEGER, FOREIGN KEY)
- `product_name` (VARCHAR)
- `quantity` (INTEGER)
- `price` (DECIMAL)

## Dependencies

- **pandas**: Data manipulation and CSV export
- **fastapi**: Modern web framework for API development
- **uvicorn**: ASGI server for FastAPI
- **faker**: Synthetic data generation

## Data Flow

1. **Setup**: `db/main.py` creates database schema and generates sample data
2. **API**: `api.py` serves REST endpoints for data retrieval
3. **ETL**: `process/etl_customer_totals.py` transforms data into summary reports

## Testing

Use tools like Postman, curl, or browser to test API endpoints. The API includes automatic interactive documentation at `http://127.0.0.1:8000/docs` when running.

## Notes

- Database is recreated each time `db/main.py` is run
- Sample data is randomly generated using Faker library
- ETL process joins customer and order data to calculate total spending per order
- All data is stored locally in SQLite database

---

## Notes
- Ensure the virtual environment is activated before running any commands.







