from src.database import MySQLConnectionManager
from src.execute_sql_file import SQLFileExecutor
import os


def main() -> None:
    my_sql_connection_manager = MySQLConnectionManager()
    sql_executor = SQLFileExecutor(my_sql_connection_manager)

    sql_executor.execute_sql_file('sql/schema.sql') 
    sql_executor.execute_sql_file('sql/data.sql')


if __name__ == "__main__":
    main()