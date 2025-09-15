from src.entity import SpeedCamera, Driver, Offense
import logging

logging.basicConfig(level=logging.DEBUG)

def main() -> None:
    logging.info("Creating entities...")
    camera = SpeedCamera(id_=1, location="Main St", allowed_speed=60)
    driver = Driver(id_=1, first_name="John", last_name="Doe", registration_number="XYZ123")
    offence = Offense(id_=1, description="Speeding", penalty_points=3, fine_amount=100)
    logging.info("Entities created successfully.")          
    logging.info(f"SpeedCamera: {camera}")
    logging.info(f"Driver: {driver}")
    logging.info(f"Offence: {offence}")    


if __name__ == '__main__':
    main()