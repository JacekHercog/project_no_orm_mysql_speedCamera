from mysql.connector import Error
from src.database import with_db_connection, MySQLConnectionManager
from typing import TYPE_CHECKING


class SQLFileExecutor:
    def __init__(self, connection_manager: MySQLConnectionManager):
        self._connection_manager = connection_manager       
    
    @with_db_connection
    def execute_sql_file(self, file_path: str) -> None:
        try:
            with open(file_path, 'r') as sql_file:
                sql_commands = sql_file.read()
            
            conn = self._connection_manager.get_connection()
            cursor = conn.cursor()
    
            for command in sql_commands.split(';'):
                command = command.strip()
                if command:
                    print(f"Executing command: {command[:30]}...")  # Print first 30 chars
                    cursor.execute(command)
            conn.commit()
            cursor.close()
            print(f"Executed SQL file: {file_path}")
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Error as e:
            print(f"Error executing SQL file: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
        