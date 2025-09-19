-- Wstawianie danych do tabeli speed_cameras
INSERT INTO speed_cameras (location, allowed_speed) VALUES
('Warsaw', 50),
('Krakow', 40),
('Gdansk', 60),
('Wroclaw', 50);

-- Wstawianie danych do tabeli drivers
INSERT INTO drivers (first_name, last_name, registration_number) VALUES
('John', 'Doe', 'K123456'),
('Jane', 'Smith', 'A987654'),
('Robert', 'Brown', 'Z567890'),
('Emily', 'Jones', 'B765432');

-- Wstawianie danych do tabeli offenses
INSERT INTO offenses (description, penalty_points, fine_amount) VALUES
('Speeding over 20 km/h', 3, 100.0),
('Red light violation', 4, 200.0),
('No seatbelt', 2, 50.0),
('Illegal parking', 0, 30.0);

-- Wstawianie danych do tabeli violations
INSERT INTO violations (violation_date, driver_id, speed_camera_id, offense_id) VALUES
('2024-01-10', 1, 2, 1),
('2024-01-11', 2, 1, 3),
('2024-01-12', 3, 3, 2),
('2024-01-15', 4, 4, 4);