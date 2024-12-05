-- Create database
CREATE DATABASE NiceDB;

-- Create STORE table
CREATE TABLE store (
    storeNumber INTEGER PRIMARY KEY,
    storeName VARCHAR(100) NOT NULL,
    storePhoneNumber VARCHAR(15) NOT NULL,
    storeEmailAddress VARCHAR(100) NOT NULL,
    storeFaxNumber VARCHAR(15),
    storeStreetNumber VARCHAR(10) NOT NULL,
    storeSuburb VARCHAR(50) NOT NULL,
    storeState CHAR(3) NOT NULL,
    storePostCode CHAR(4) NOT NULL
);

-- Create DEPARTMENT table
CREATE TABLE department (
    departmentNumber INTEGER PRIMARY KEY,
    departmentTitle VARCHAR(50) NOT NULL,
    departmentPhoneNumber VARCHAR(15) NOT NULL,
    departmentEmailAddress VARCHAR(100) NOT NULL,
    storeNumber INTEGER NOT NULL,
    managerEmployeeNumber INTEGER,
    FOREIGN KEY (storeNumber) REFERENCES store(storeNumber)
);

-- Create EMPLOYEE table
CREATE TABLE employee (
    employeeNumber INTEGER PRIMARY KEY,
    employeeFirstName VARCHAR(50) NOT NULL,
    employeeLastName VARCHAR(50) NOT NULL,
    employeeAddress VARCHAR(200) NOT NULL,
    employeeMobileNumber VARCHAR(15) NOT NULL,
    employeeEmailAddress VARCHAR(100) NOT NULL,
    taxFileNumber VARCHAR(9) NOT NULL UNIQUE,
    salaryHourlyRate DECIMAL(10,2) NOT NULL,
    employmentType CHAR(1) NOT NULL CHECK (employmentType IN ('F', 'P', 'C')), -- Full-time, Part-time, Casual
    joiningDate DATE NOT NULL,
    storeNumber INTEGER NOT NULL,
    departmentNumber INTEGER NOT NULL,
    managerEmployeeNumber INTEGER,
    FOREIGN KEY (storeNumber) REFERENCES store(storeNumber),
    FOREIGN KEY (departmentNumber) REFERENCES department(departmentNumber),
    FOREIGN KEY (managerEmployeeNumber) REFERENCES employee(employeeNumber)
);

-- Add foreign key constraint to department after employee table creation
ALTER TABLE department 
ADD CONSTRAINT fk_manager 
FOREIGN KEY (managerEmployeeNumber) REFERENCES employee(employeeNumber);

-- Create SUPPLIER table
CREATE TABLE supplier (
    supplierNumber INTEGER PRIMARY KEY,
    supplierName VARCHAR(100) NOT NULL,
    supplierPhoneNumber VARCHAR(15) NOT NULL,
    supplierEmailAddress VARCHAR(100) NOT NULL,
    supplierAddress VARCHAR(200) NOT NULL
);

-- Create PRODUCT table
CREATE TABLE product (
    productNumber INTEGER PRIMARY KEY,
    productName VARCHAR(100) NOT NULL,
    brand VARCHAR(50) NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL
);

-- Create PRODUCT_SUPPLIER junction table
CREATE TABLE product_supplier (
    productNumber INTEGER,
    supplierNumber INTEGER,
    PRIMARY KEY (productNumber, supplierNumber),
    FOREIGN KEY (productNumber) REFERENCES product(productNumber),
    FOREIGN KEY (supplierNumber) REFERENCES supplier(supplierNumber)
);

-- Create INVENTORY table
CREATE TABLE inventory (
    storeNumber INTEGER,
    productNumber INTEGER,
    quantityAvailable INTEGER NOT NULL CHECK (quantityAvailable >= 0),
    quantityOrdered INTEGER NOT NULL CHECK (quantityOrdered >= 0),
    PRIMARY KEY (storeNumber, productNumber),
    FOREIGN KEY (storeNumber) REFERENCES store(storeNumber),
    FOREIGN KEY (productNumber) REFERENCES product(productNumber)
);

-- Create CUSTOMER table
CREATE TABLE customer (
    customerNumber INTEGER PRIMARY KEY,
    customerFirstName VARCHAR(50) NOT NULL,
    customerLastName VARCHAR(50) NOT NULL,
    customerMobileNumber VARCHAR(15) NOT NULL,
    customerAddress VARCHAR(200) NOT NULL
);

-- Create ORDER table
CREATE TABLE "order" (
    orderNumber INTEGER PRIMARY KEY,
    orderDate DATE NOT NULL,
    storeNumber INTEGER NOT NULL,
    customerNumber INTEGER NOT NULL,
    shippingAddress VARCHAR(200) NOT NULL,
    FOREIGN KEY (storeNumber) REFERENCES store(storeNumber),
    FOREIGN KEY (customerNumber) REFERENCES customer(customerNumber)
);

-- Create ORDER_PRODUCT junction table
CREATE TABLE order_product (
    orderNumber INTEGER,
    productNumber INTEGER,
    quantityOrdered INTEGER NOT NULL CHECK (quantityOrdered > 0),
    PRIMARY KEY (orderNumber, productNumber),
    FOREIGN KEY (orderNumber) REFERENCES "order"(orderNumber),
    FOREIGN KEY (productNumber) REFERENCES product(productNumber)
);

-- Create PAYSLIP table
CREATE TABLE payslip (
    paySlipNumber INTEGER PRIMARY KEY,
    employeeNumber INTEGER NOT NULL,
    storeNumber INTEGER NOT NULL,
    hoursWorked DECIMAL(5,2) NOT NULL,
    grossPay DECIMAL(10,2) NOT NULL,
    superannuationPaid DECIMAL(10,2) NOT NULL,
    payPeriodStartDate DATE NOT NULL,
    payPeriodEndDate DATE NOT NULL,
    FOREIGN KEY (employeeNumber) REFERENCES employee(employeeNumber),
    FOREIGN KEY (storeNumber) REFERENCES store(storeNumber)
);

-- Insert sample data for each table
-- Store data
INSERT INTO store VALUES 
(1, 'Nice Store CBD', '0291234567', 'cbd@nicestore.com', '0291234568', '123', 'Sydney', 'NSW', '2000'),
(2, 'Nice Store Parramatta', '0298765432', 'parra@nicestore.com', '0298765433', '45', 'Parramatta', 'NSW', '2150'),
(3, 'Nice Store Chatswood', '0294567890', 'chats@nicestore.com', '0294567891', '78', 'Chatswood', 'NSW', '2067'),
(4, 'Nice Store Bondi', '0292345678', 'bondi@nicestore.com', '0292345679', '90', 'Bondi', 'NSW', '2026'),
(5, 'Nice Store Miranda', '0295678901', 'miranda@nicestore.com', '0295678902', '34', 'Miranda', 'NSW', '2228');

-- Department data
INSERT INTO department VALUES
(101, 'Electronics', '0291234567', 'electronics@nicestore.com', 1, NULL),
(102, 'Home & Living', '0291234568', 'homeliving@nicestore.com', 1, NULL),
(103, 'Fashion', '0298765432', 'fashion@nicestore.com', 2, NULL),
(104, 'Sports', '0294567890', 'sports@nicestore.com', 3, NULL),
(105, 'Beauty', '0292345678', 'beauty@nicestore.com', 4, NULL);

-- Employee data
INSERT INTO employee VALUES
(1001, 'John', 'Smith', '123 Park Rd, Sydney', '0400111222', 'john.smith@nicestore.com', '123456789', 35.50, 'F', '2020-01-15', 1, 101, NULL),
(1002, 'Sarah', 'Johnson', '45 Queen St, Parramatta', '0400222333', 'sarah.j@nicestore.com', '234567890', 28.75, 'P', '2020-03-20', 2, 103, 1001),
(1003, 'Michael', 'Wong', '67 Victoria Ave, Chatswood', '0400333444', 'michael.w@nicestore.com', '345678901', 32.00, 'F', '2020-06-10', 3, 104, 1001),
(1004, 'Emma', 'Brown', '89 Beach Rd, Bondi', '0400444555', 'emma.b@nicestore.com', '456789012', 26.50, 'C', '2021-01-05', 4, 105, 1001),
(1005, 'David', 'Lee', '12 Station St, Miranda', '0400555666', 'david.l@nicestore.com', '567890123', 30.25, 'F', '2021-03-15', 5, 102, 1001);

-- Update department managers
UPDATE department SET managerEmployeeNumber = 1001 WHERE departmentNumber = 101;
UPDATE department SET managerEmployeeNumber = 1002 WHERE departmentNumber = 103;
UPDATE department SET managerEmployeeNumber = 1003 WHERE departmentNumber = 104;
UPDATE department SET managerEmployeeNumber = 1004 WHERE departmentNumber = 105;
UPDATE department SET managerEmployeeNumber = 1005 WHERE departmentNumber = 102;

-- Supplier data
INSERT INTO supplier VALUES
(201, 'Tech Supplies Co', '0298901234', 'sales@techsupplies.com', '123 Industrial Ave, Alexandria NSW 2015'),
(202, 'Home Essentials Ltd', '0297892345', 'orders@homeessentials.com', '456 Business Park, Mascot NSW 2020'),
(203, 'Fashion Forward Pty', '0296783456', 'contact@fashionforward.com', '789 Style St, Surry Hills NSW 2010'),
(204, 'Sports Gear Direct', '0295674567', 'info@sportsgear.com', '321 Athletic Way, Homebush NSW 2140'),
(205, 'Beauty Basics Inc', '0294565678', 'sales@beautybasics.com', '654 Glamour Rd, Double Bay NSW 2028');

-- Product data
INSERT INTO product VALUES
(301, 'Smart TV 55"', 'Samsung', '4K Ultra HD Smart TV', 999.99),
(302, 'Sofa Set', 'HomeStyle', 'Three-seater with two recliners', 1499.99),
(303, 'Designer Jeans', 'Levis', 'Classic fit blue jeans', 89.99),
(304, 'Tennis Racket', 'Wilson', 'Professional grade tennis racket', 199.99),
(305, 'Skincare Set', 'Clinique', 'Complete skincare routine set', 149.99);

-- Product_Supplier data
INSERT INTO product_supplier VALUES
(301, 201),
(302, 202),
(303, 203),
(304, 204),
(305, 205);

-- Inventory data
INSERT INTO inventory VALUES
(1, 301, 10, 5),
(2, 302, 8, 3),
(3, 303, 15, 10),
(4, 304, 12, 6),
(5, 305, 20, 8);

-- Customer data
INSERT INTO customer VALUES
(401, 'Alice', 'Wilson', '0411222333', '123 Customer St, Sydney NSW 2000'),
(402, 'Bob', 'Taylor', '0422333444', '456 Buyer Rd, Parramatta NSW 2150'),
(403, 'Carol', 'Martinez', '0433444555', '789 Shop Ave, Chatswood NSW 2067'),
(404, 'Daniel', 'Anderson', '0444555666', '321 Client Pl, Bondi NSW 2026'),
(405, 'Eva', 'Chen', '0455666777', '654 Consumer Ln, Miranda NSW 2228');

-- Order data
INSERT INTO "order" VALUES
(501, '2023-03-01', 1, 401, '123 Customer St, Sydney NSW 2000'),
(502, '2023-03-02', 2, 402, '456 Buyer Rd, Parramatta NSW 2150'),
(503, '2023-03-03', 3, 403, '789 Shop Ave, Chatswood NSW 2067'),
(504, '2023-03-04', 4, 404, '321 Client Pl, Bondi NSW 2026'),
(505, '2023-03-05', 5, 405, '654 Consumer Ln, Miranda NSW 2228');

-- Order_Product data
INSERT INTO order_product VALUES
(501, 301, 1),
(502, 302, 1),
(503, 303, 2),
(504, 304, 1),
(505, 305, 3);

-- Payslip data
INSERT INTO payslip VALUES
(601, 1001, 1, 38.0, 1349.00, 127.65, '2023-03-01', '2023-03-14'),
(602, 1002, 2, 20.0, 575.00, 54.62, '2023-03-01', '2023-03-14'),
(603, 1003, 3, 38.0, 1216.00, 115.52, '2023-03-01', '2023-03-14'),
(604, 1004, 4, 15.0, 397.50, 37.76, '2023-03-01', '2023-03-14'),
(605, 1005, 5, 38.0, 1149.50, 109.20, '2023-03-01', '2023-03-14');

-- Select all columns from the employee table
SELECT * FROM employee;

-- Select all columns from the store table
SELECT * FROM store;

-- Select all columns from the department table
SELECT * FROM department;

-- Select all columns from the supplier table
SELECT * FROM supplier;

-- Select all columns from the product table
SELECT * FROM product;

-- Select all columns from the product_supplier table
SELECT * FROM product_supplier;

-- Select all columns from the inventory table
SELECT * FROM inventory;

-- Select all columns from the customer table
SELECT * FROM customer;

-- Select all columns from the "order" table (note the quotes around "order" since it's a reserved keyword)
SELECT * FROM "order";

-- Select all columns from the order_product table
SELECT * FROM order_product;

-- Select all columns from the payslip table
SELECT * FROM payslip;


-- \d store
-- \d department
-- \d employee
-- \d supplier
-- \d product
-- \d product_supplier
-- \d inventory
-- \d customer
-- \d "order"
-- \d order_product
-- \d payslip