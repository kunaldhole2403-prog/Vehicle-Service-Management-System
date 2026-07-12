-- Login Table
CREATE TABLE Login(
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    role VARCHAR(20) NOT NULL
);

-- Customer Table
CREATE TABLE Customer(
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(50) NOT NULL,
    phone VARCHAR(15),
    email VARCHAR(50),
    address VARCHAR(100)
);

-- Vehicle Table
CREATE TABLE Vehicle(
    vehicle_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    vehicle_no VARCHAR(20) UNIQUE,
    company VARCHAR(30),
    model VARCHAR(30),
    year INT,
    FOREIGN KEY(customer_id)
    REFERENCES Customer(customer_id)
);

CREATE TABLE Service_Master (
    service_master_id INT AUTO_INCREMENT PRIMARY KEY,
    service_name VARCHAR(50) NOT NULL,
    price DECIMAL(10,2) NOT NULL
);

CREATE TABLE Service_Record (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    vehicle_id INT NOT NULL,
    service_date DATE NOT NULL,
    status VARCHAR(20) NOT NULL,
    FOREIGN KEY(vehicle_id)
    REFERENCES Vehicle(vehicle_id)
);
CREATE TABLE Service_Details (
    detail_id INT AUTO_INCREMENT PRIMARY KEY,
    service_id INT NOT NULL,
    service_master_id INT NOT NULL,

    FOREIGN KEY(service_id)
    REFERENCES Service_Record(service_id),

    FOREIGN KEY(service_master_id)
    REFERENCES Service_Master(service_master_id)
);
-- Billing Table
CREATE TABLE Billing(
    bill_id INT AUTO_INCREMENT PRIMARY KEY,
    service_id INT,
    amount DECIMAL(10,2),
    payment_status VARCHAR(20),
    bill_date DATE,
    FOREIGN KEY(service_id)
    REFERENCES Service(service_id)
);
