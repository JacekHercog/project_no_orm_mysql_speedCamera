from src.entity import Driver, Offense, Violation, SpeedCamera, Entity
from src.database import with_db_connection, MySQLConnectionManager
from typing import Generator, TYPE_CHECKING
import inflection

# added for mypy
if TYPE_CHECKING:
    from mysql.connector import MySQLConnection
    from mysql.connector.cursor import MySQLCursor


class CrudRepository[T: Entity]:
    def __init__(self, connection_manager: MySQLConnectionManager, entity_type: type[T]):
        self._connection_manager = connection_manager
        self._entity_type = entity_type
        # Add attributes for mypy
        self._conn: 'MySQLConnection'
        self._cursor: 'MySQLCursor'

    # tree types of fetching data
    # 1. fetchall() - get all data at once into a list and you have to wait until it is created
    # 2. fetchmany(size=n) - get portion of data, in this case n records
    # 3. iterator - each iteration contains a single record, you fetch row by row
    
    @with_db_connection
    def find_all(self) -> list[T]:
        sql = f"select * from {self._table_name()}"
        self._cursor.execute(sql)

        # get all data at once into a list and you have to wait until it is created
        return [self._entity_type.from_row(row) for row in self._cursor.fetchall()]
    
    @with_db_connection
    def find_all_by_portion(self, size_portion: int = 500) -> list[T]:
        sql = f"select * from {self._table_name()}"
        self._cursor.execute(sql)

        # get portion of data, in this case 500 records
        rows = []
        while True:
            data = self._cursor.fetchmany(size=size_portion)  # get portion of data, in this case 500 records
            if not data:
                break
            rows.extend([self._entity_type.from_row(row) for row in data])
        return rows
    
    # Method 3: Returns generator (no return needed)
    @with_db_connection
    def find_all_streaming(self) -> Generator[T, None, None]:
        sql = f"select * from {self._table_name()}"
        self._cursor.execute(sql)

        # Every iteration contains a single record, you fetch row by row
        # and in this way you can pull huge amounts of data
        for row in self._cursor:
            yield self._entity_type.from_row(row)

    def _table_name(self) -> str:
        return inflection.pluralize(inflection.underscore(self._entity_type.__name__))