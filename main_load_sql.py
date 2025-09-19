from src.database import MySQLConnectionManager
from src.execute_sql_file import SQLFileExecutor
import os
import logging

# Configure logging to output to console
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()  # This outputs to console
    ]
)

def main() -> None:
    my_sql_connection_manager = MySQLConnectionManager()
    sql_executor = SQLFileExecutor(my_sql_connection_manager)

    sql_executor.execute_sql_file('sql/schema.sql') 
    sql_executor.execute_sql_file('sql/data.sql')


if __name__ == "__main__":
    main()