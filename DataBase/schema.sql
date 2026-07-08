CREATE TABLE Customer(
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL,
    phone TEXT,
    email TEXT,
    address TEXT
);

CREATE TABLE Vehicle(
    vehicle_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    vehicle_no TEXT,
    company TEXT,
    model TEXT,
    year INTEGER,
    FOREIGN KEY(customer_id)
    REFERENCES Customer(customer_id)
);

CREATE TABLE Service(
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    vehicle_id INTEGER,
    service_type TEXT,
    service_date DATE,
    status TEXT,
    FOREIGN KEY(vehicle_id)
    REFERENCES Vehicle(vehicle_id)
);

CREATE TABLE Mechanic(
    mechanic_id INTEGER PRIMARY KEY AUTOINCREMENT,
    mechanic_name TEXT,
    phone TEXT,
    specialization TEXT
);


CREATE TABLE Service_Assignment(
    assign_id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_id INTEGER,
    mechanic_id INTEGER,
    FOREIGN KEY(service_id)
    REFERENCES Service(service_id),
    FOREIGN KEY(mechanic_id)
    REFERENCES Mechanic(mechanic_id)
);


CREATE TABLE Billing(
    bill_id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_id INTEGER,
    amount REAL,
    payment_status TEXT,
    bill_date DATE,
    FOREIGN KEY(service_id)
    REFERENCES Service(service_id)
);