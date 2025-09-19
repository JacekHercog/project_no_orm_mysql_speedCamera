from dotenv import load_dotenv
from typing import Callable, Any
import inspect
from types import GeneratorType
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
        # Check if the function is a generator function
        if inspect.isgeneratorfunction(func):
            # For generators, we need to keep the connection open
            conn = self._connection_manager.get_connection()
            cursor = conn.cursor()
            try:
                self._conn = conn
                self._cursor = cursor
                generator = func(self, *args, **kwargs)
                
                # Wrap the generator to handle cleanup
                def generator_wrapper():
                    try:
                        yield from generator
                    finally:
                        cursor.close()
                        conn.close()   
                return generator_wrapper()
            except Exception as e:
                cursor.close()
                conn.rollback()
                conn.close()
                raise e
        else:
            # For regular functions, use context manager
            with (
                self._connection_manager.get_connection() as conn,
                conn.cursor() as cursor
            ):
                try:
                    self._conn = conn
                    self._cursor = cursor
                    result = func(self, *args, **kwargs)
                    self._conn.commit()
                    return result
                except Exception as e:
                    if self._conn:
                        self._conn.rollback()
                    raise e      
    return wrapper