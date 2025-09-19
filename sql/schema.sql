CREATE TABLE IF NOT EXISTS speed_cameras (
    id_ INT PRIMARY KEY AUTO_INCREMENT,
    location VARCHAR(255) NOT NULL,
    allowed_speed INT NOT NULL
);

CREATE TABLE IF NOT EXISTS drivers (
    id_ INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    registration_number VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS offenses (
    id_ INT PRIMARY KEY AUTO_INCREMENT,
    description VARCHAR(255) NOT NULL,
    penalty_points INT NOT NULL,
    fine_amount DECIMAL(10, 2) NOT NULL
);

CREATE TABLE IF NOT EXISTS violations (
    id_ INT PRIMARY KEY AUTO_INCREMENT,
    violation_date DATE NOT NULL,
    driver_id INT,
    speed_camera_id INT,
    offense_id INT,
    FOREIGN KEY (driver_id) REFERENCES drivers(id_) ON DELETE CASCADE,
    FOREIGN KEY (speed_camera_id) REFERENCES speed_cameras(id_) ON DELETE CASCADE,
    FOREIGN KEY (offense_id) REFERENCES offenses(id_) ON DELETE CASCADE
);