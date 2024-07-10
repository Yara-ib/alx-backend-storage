# SQL || MySQL

## 1. Creating Tables with Constraints
Constraints in SQL are used to specify rules for the data in a table. These rules ensure the accuracy and reliability of the data. Common constraints include PRIMARY KEY, FOREIGN KEY, UNIQUE, NOT NULL, and CHECK.

### Example: Creating a Table with Constraints

```
CREATE TABLE employees (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,  -- Primary Key constraint
    first_name VARCHAR(50) NOT NULL,        -- NOT NULL constraint
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,              -- UNIQUE constraint
    hire_date DATE NOT NULL,
    job_id INT,
    salary DECIMAL(8, 2) CHECK (salary > 0) -- CHECK constraint
);
```

```
CREATE TABLE jobs (
    job_id INT AUTO_INCREMENT PRIMARY KEY,
    job_title VARCHAR(50) NOT NULL
);
```

```
ALTER TABLE employees
ADD CONSTRAINT fk_job
FOREIGN KEY (job_id) REFERENCES jobs(job_id); -- FOREIGN KEY constraint
```

## 2. Optimizing Queries by Adding Indexes
Indexes are used to speed up the retrieval of rows by using a pointer. Indexes can be created on a single column or a combination of columns.

### Example: Adding an Index

```
CREATE INDEX idx_last_name ON employees(last_name);
```

```
-- Composite index on multiple columns
CREATE INDEX idx_first_last_name ON employees(first_name, last_name);
```

## 3. Stored Procedures and Functions in MySQL
Stored Procedures: These are stored code that can be executed and reused. They can have input and output parameters.

### Example: Creating a Stored Procedure
```
DELIMITER //

CREATE PROCEDURE GetEmployee(IN emp_id INT)
BEGIN
    SELECT * FROM employees WHERE emp_id = emp_id;
END //

DELIMITER ;
```

```
-- Calling the stored procedure
CALL GetEmployee(1);
```
## Functions: These return a single value and can be used in SQL statements.

### Example: Creating a Function
```
DELIMITER //

CREATE FUNCTION CalculateBonus(salary DECIMAL(8, 2))
RETURNS DECIMAL(8, 2)
BEGIN
    RETURN salary * 0.1;
END //

DELIMITER ;
```

```
-- Using the function
SELECT first_name, last_name, CalculateBonus(salary) AS bonus FROM employees;
```

## 4. Views in MySQL
A view is a virtual table based on the result set of an SQL statement. Views can be used to simplify complex queries, improve security, and provide a level of abstraction.

### Example: Creating a View
```
CREATE VIEW EmployeeDetails AS
SELECT e.emp_id, e.first_name, e.last_name, j.job_title
FROM employees e
JOIN jobs j ON e.job_id = j.job_id;
```

```
-- Using the view
SELECT * FROM EmployeeDetails;
```

## 5. Triggers in MySQL
Triggers are database callbacks that are automatically executed or fired when certain events occur.

### Example: Creating a Trigger
```
DELIMITER //

CREATE TRIGGER before_employee_insert
BEFORE INSERT ON employees
FOR EACH ROW
BEGIN
    IF NEW.salary < 0 THEN
        SET NEW.salary = 0;
    END IF;
END //

DELIMITER ;
```

## 6. MySQL Performance: Leveraging Database Indexing
Indexes improve the speed of data retrieval operations on a database table at the cost of additional storage and slower writes.

### Example: Creating an Index
```
CREATE INDEX idx_emp_last_name ON employees(last_name);

-- Analyzing query performance using EXPLAIN
EXPLAIN SELECT * FROM employees WHERE last_name = 'Smith';
```

## 7. CREATE TABLE Statement
The CREATE TABLE statement is used to create a new table in a database.

### Example: CREATE TABLE
```
CREATE TABLE departments (
    dept_id INT AUTO_INCREMENT PRIMARY KEY,
    dept_name VARCHAR(100) NOT NULL
);
```

## 8. CREATE PROCEDURE and CREATE FUNCTION Statements
### Stored Procedure Example:
```
DELIMITER //

CREATE PROCEDURE AddEmployee(IN first_name VARCHAR(50), IN last_name VARCHAR(50), IN email VARCHAR(100), IN hire_date DATE, IN job_id INT, IN salary DECIMAL(8, 2))
BEGIN
    INSERT INTO employees (first_name, last_name, email, hire_date, job_id, salary)
    VALUES (first_name, last_name, email, hire_date, job_id, salary);
END //

DELIMITER ;
```

### Function Example:
```
DELIMITER //

CREATE FUNCTION GetFullName(emp_id INT)
RETURNS VARCHAR(101)
BEGIN
    DECLARE full_name VARCHAR(101);
    SELECT CONCAT(first_name, ' ', last_name) INTO full_name
    FROM employees WHERE emp_id = emp_id;
    RETURN full_name;
END //

DELIMITER ;
```

## 9. CREATE INDEX Statement
The CREATE INDEX statement is used to create indexes on tables.

### Example: CREATE INDEX
```
CREATE INDEX idx_email ON employees(email);
```

## 10. CREATE VIEW Statement
The CREATE VIEW statement is used to create a view.

### Example: CREATE VIEW
```
CREATE VIEW EmployeeOverview AS
SELECT emp_id, first_name, last_name, salary
FROM employees;
```
