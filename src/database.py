from dotenv import load_dotenv
from typing import Callable, Any
import os
from mysql.connector import MySQLConnection, pooling

load_dotenv()


class MySQLConnectionManager:
    def __init__(self) -> None:
        self._pool =  pooling.MySQLConnectionPool(
            pool_name='mysql_pool',
            pool_size=int(os.getenv('MYSQL_POOL_SIZE', 5)),
            host=os.getenv('MYSQL_HOST'),
            database=os.getenv('MYSQL_DATABASE'),
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PASSWORD'),
            port=int(os.getenv('MYSQL_PORT', 3307))
        )

    def get_connection(self):
        return self._pool.get_connection()
    
# Dekorator, ktory pozwoli skorzystac z polaczenia z baza danych nad metoda,
# nad ktora go umiescimy
def with_db_connection(func:Callable)-> Callable:
    def wrapper(self,*args: Any, **kwargs:Any) -> Any:
        with self._connection_manager.get_connection() as conn:
            self._conn = conn
            self._cursor = conn.cursor()
        try:
            result = func(self, *args, **kwargs)
            self._conn.commit()
            return result
        except Exception as e:
            self._conn.rollback()
            raise e
        finally:
            self._cursor.close()
            self._conn.close()
    return wrapper