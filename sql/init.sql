CREATE DATABASE productdb;

CREATE TABLE products(
 product_id SERIAL PRIMARY KEY,
 product_name VARCHAR(100),
 price NUMERIC
);

INSERT INTO products(product_name,price)
VALUES
('Laptop',50000),
('Mobile',20000),
('Monitor',15000),
('Keyboard',1000),
('Mouse',500);

SELECT * FROM products;

SELECT current_database();

SELECT table_name
FROM information_schema.tables
WHERE table_schema='public';

SELECT version();

\c productdb