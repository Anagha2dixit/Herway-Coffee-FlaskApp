-- Drop existing customers table
DROP TABLE IF EXISTS customers;

-- Recreate with loyalty_points column
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    phone TEXT,
    address TEXT,
    loyalty_points INTEGER DEFAULT 0
);

-- Reinsert old records with loyalty_points = 0
INSERT INTO customers (customer_id, name, email, phone, address, loyalty_points)
VALUES
(1, 'Alice', 'alice@example.com', '1234567890', 'Downtown Street', 0),
(2, 'Bob', 'bob@example.com', '9876543210', 'Market Road', 0);
