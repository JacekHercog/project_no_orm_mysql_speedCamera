from src.entity import SpeedCamera, Driver, Offense
from src.repository import DriverRepository, OffenseRepository, SpeedCameraRepository
from src.database import MySQLConnectionManager
import logging

logging.basicConfig(level=logging.DEBUG)

def main() -> None:
    # logging.info("Creating entities...")
    # camera = SpeedCamera(id_=1, location="Main St", allowed_speed=60)
    # driver = Driver(id_=1, first_name="John", last_name="Doe", registration_number="XYZ123")
    # offence = Offense(id_=1, description="Speeding", penalty_points=3, fine_amount=100)
    # logging.info("Entities created successfully.")          
    # logging.info(f"SpeedCamera: {camera}")
    # logging.info(f"Driver: {driver}")
    # logging.info(f"Offence: {offence}") 
    # 
    logging.info("Creating repositories...")
    connection_manager = MySQLConnectionManager()
    driver_repository = DriverRepository(connection_manager)

    # driver_repository.insert(Driver(first_name="Jacek", last_name="Hercog",registration_number="ABC123"))
    # driver_repository.insert(Driver(first_name="Joanna", last_name="Hercog",registration_number="CBA123"))

    logging.info("Repositories created successfully.")  
    logging.info("--------------------------------")
    logging.info("Fetching all drivers...") 
    for driver in driver_repository.find_all():
        logging.info(f"Driver: {driver}")  

    logging.info("--------------------------------")
    logging.info("Fetching drivers by portion of 2...")
    for driver in driver_repository.find_all_by_portion(2):
        logging.info(f"Driver: {driver}")

    logging.info("--------------------------------")
    logging.info("Fetching drivers using streaming...")
    for driver in driver_repository.find_all_streaming():
        logging.info(f"Driver: {driver}")

    logging.info("--------------------------------")
    logging.info("Fetching driver by ID...")
    driver = driver_repository.find_by_id(5)
    logging.info(f"Driver: {driver}")

    logging.info("--------------------------------")
    logging.info("Updating driver...")
    driver_update = Driver(id_=5, first_name="Jan", last_name="Kowalski", registration_number="XYZ789")
    driver_repository.update(5, driver_update)
    driver = driver_repository.find_by_id(5)
    logging.info(f"Updated Driver: {driver}")

    logging.info("--------------------------------")
    logging.info("Deleting driver...")
    driver_repository.delete(5)
    driver = driver_repository.find_by_id(5)
    logging.info(f"Deleted Driver (should be None): {driver}")
    
    logging.info("Insert multiple drivers...")
    driver_repository.insert_many([
        Driver(first_name="AAA", last_name="`BBB`", registration_number="AAA111"),
        Driver(first_name="CCC", last_name="DDD", registration_number="BBB222"),
        Driver(first_name="EEE", last_name="FFF", registration_number="CCC333"),
    ], batch_size=2)
    for driver in driver_repository.find_all_by_portion():
        logging.info(f"Driver: {driver}")

    logging.info('Insert multiple insert to many executemany')
    driver_repository.insert_many_optimized([
        Driver(first_name="AAA111", last_name="BBB111", registration_number="AAA111"),
        Driver(first_name="CCC111", last_name="DDD111", registration_number="BBB222"),
        Driver(first_name="EEE111", last_name="FFF111", registration_number="CCC333"),
        Driver(first_name="GGG111", last_name="HHH111", registration_number="DDD444"),
        Driver(first_name="III111", last_name="JJJ111", registration_number="EEE555")
    ], batch_size=2)

    for driver in driver_repository.find_all_streaming():
        logging.info(f"Driver: {driver}")


if __name__ == '__main__':
    main()