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

    # driver_epository.insert(Driver(first_name="Jacek", last_name="Hercog",registration_number="ABC123"))
    driver_repository.insert(Driver(first_name="Joanna", last_name="Hercog",registration_number="CBA123"))

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


if __name__ == '__main__':
    main()