-- Insert into customers
INSERT INTO customers VALUES
(1, 'Alice', 'alice@example.com', '1234567890', 'Downtown Street'),
(2, 'Bob', 'bob@example.com', '9876543210', 'Market Road');

-- Insert into products
INSERT INTO products VALUES
(101, 'Espresso Beans', 'Coffee', 450.00, 100),
(102, 'French Press', 'Equipment', 1200.00, 20),
(103, 'Cold Brew Bottle', 'Drink', 150.00, 50);

-- Insert into orders
INSERT INTO orders VALUES
(201, 1, '2025-07-01'),
(202, 2, '2025-07-02');

-- Insert into order_items
INSERT INTO order_items VALUES
(1, 201, 101, 2),
(2, 201, 103, 1),
(3, 202, 102, 1);
