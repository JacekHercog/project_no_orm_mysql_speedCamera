from mysql.connector import Error
from src.database import with_db_connection, MySQLConnectionManager
import logging

logger = logging.getLogger(__name__)    

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
                    logger.info(f"Executing command:\n {command}")
                    cursor.execute(command)
            conn.commit()
            cursor.close()
            logger.info(f"Executed SQL file: {file_path}")
        except Error as e:
            logger.error(f"Error executing SQL file: {e}")
            raise e

