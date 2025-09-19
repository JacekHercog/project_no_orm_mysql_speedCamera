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
        return [self._entity_type.from_row(*row) for row in self._cursor.fetchall()]
    
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
            rows.extend([self._entity_type.from_row(*row) for row in data])
        return rows
    
    # Method 3: Returns generator (no return needed)
    @with_db_connection
    def find_all_streaming(self) -> Generator[T, None, None]:
        sql = f"select * from {self._table_name()}"
        self._cursor.execute(sql)

        # Every iteration contains a single record, you fetch row by row
        # and in this way you can pull huge amounts of data
        for row in self._cursor:
            yield self._entity_type.from_row(*row)
        
    @with_db_connection
    def insert(self, item: T) -> int:
        sql = (f'insert into {self._table_name()} '
               f'({self._column_names_for_insert()}) '
               f'values ({self._column_values_for_insert(item)})')
        print(f'INSERT: {sql}')
        self._cursor.execute(sql)
        return self._cursor.lastrowid if self._cursor.lastrowid else 0

    def _table_name(self) -> str:
        return inflection.pluralize(inflection.underscore(self._entity_type.__name__))
    
    def _column_names_for_insert(self) -> str:
        return ', '.join([field for field in self._entity_type.__annotations__.keys() if field != 'id_'])

    def _column_values_for_insert(self, item: T) -> str:
        fields = [field for field in self._entity_type.__annotations__.keys() if field != 'id_']
        values = [
            str(getattr(item, field)) if isinstance(getattr(item, field), (int, float))
            else f"'{getattr(item, field)}'"
            for field in fields
        ]
        return ', '.join(values)

class DriverRepository(CrudRepository[Driver]):
    def __init__(self, connection_manager: MySQLConnectionManager):
        super().__init__(connection_manager, Driver)

class SpeedCameraRepository(CrudRepository[SpeedCamera]):
    def __init__(self, connection_manager: MySQLConnectionManager):
        super().__init__(connection_manager, SpeedCamera)

class OffenseRepository(CrudRepository[Offense]):
    def __init__(self, connection_manager: MySQLConnectionManager):
        super().__init__(connection_manager, Offense)

class ViolationRepository(CrudRepository[Violation]):
    def __init__(self, connection_manager: MySQLConnectionManager):
        super().__init__(connection_manager, Violation)