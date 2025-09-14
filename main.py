from src.entity import SpeedCamera, Driver, Offence
import logging

logging.basicConfig(level=logging.DEBUG)

def main() -> None:
    logging.info("Creating entities...")
    camera = SpeedCamera(id_=1, location="Main St", allowed_speed=60)
    driver = Driver(id_=1, first_name="John", last_name="Doe", registration_number="XYZ123")
    offence = Offence(id_=1, description="Speeding", penalty_points=3, fine_amount=100)
    logging.info("Entities created successfully.")          
    logging.debug(f"SpeedCamera: {camera}")
    logging.debug(f"Driver: {driver}")
    logging.debug(f"Offence: {offence}")    


if __name__ == '__main__':
    main()