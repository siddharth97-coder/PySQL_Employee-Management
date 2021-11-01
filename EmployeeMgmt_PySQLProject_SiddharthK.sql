CREATE DATABASE Emp_Mgmt;
GO
USE Emp_Mgmt;
GO

CREATE TABLE addresses (
	id INT IDENTITY(1,1) PRIMARY KEY,
	street VARCHAR (50) DEFAULT NULL,
	city VARCHAR (30) NOT NULL,
	state VARCHAR (30) DEFAULT NULL,
);
GO
CREATE TABLE employees (
	id INT IDENTITY(1,1) PRIMARY KEY,
	name VARCHAR (100) NOT NULL,
	age INT NOT NULL,
	salary DECIMAL (8, 2) NOT NULL,
	d_id INT DEFAULT NOT NULL,
	a_id INT NOT NULL,
	m_id INT DEFAULT NULL ,
	FOREIGN KEY (a_id) REFERENCES addresses (id) ON DELETE CASCADE ON UPDATE CASCADE ,
	FOREIGN KEY (m_id) REFERENCES employees (id) 
);
GO
CREATE TABLE departments (
	id INT IDENTITY(1,1) PRIMARY KEY,
	name VARCHAR (100) NOT NULL,
	m_id  INT DEFAULT NULL, 
	a_id INT DEFAULT NULL , --Address ID of the department headquarters
	FOREIGN KEY (m_id)  REFERENCES employees (id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (a_id)  REFERENCES addresses (id) 
);
GO

ALTER TABLE employees ADD dept_id INT DEFAULT NULL
FOREIGN KEY (dept_id) REFERENCES departments (id);
GO
ALTER TABLE employees ALTER COLUMN a_id INT NOT NULL;
GO
ALTER TABLE employees ALTER COLUMN dept_id INT NOT NULL;
GO

--After importing the CSV file from Python script
--The full data for each Employee with their address as a string, department name, and manager name.
SELECT
	e.id 'ID', e.name 'Name', e.age 'Age', e.salary 'Salary',
	 a.street + ' ' + a.city + ' ' + a.state AS 'Address',
	 d.name AS 'Department Name',
	 m.name AS 'Manager Name'
FROM 
	employees1 e
LEFT JOIN 
	departments1 d
ON 
	e.department_id = d.id
LEFT JOIN 
	addresses1 a
ON 
	e.address_id = a.id
LEFT JOIN
	employees1 m
ON 
	e.manager_id = m.id
;

-- the 5 highest paid and lowest paid employees
--5 highest paid
SELECT 
	TOP(5) id, name, age, salary 
FROM
	employees1
ORDER BY
salary DESC;
--Lowest 5 paid

SELECT 
	TOP(5) id, name, age, salary
FROM
	employees1
ORDER BY
salary;

-- The total salary for each department, the manager's name, sorted by highest total
SELECT 
	d.name 'Department Name',
	--m.name 'Manager Name',
	SUM(e.salary) 'Total Salary'
FROM 
	departments1 d 
INNER JOIN
	employees1 e
ON
	 d.id = e.department_id
LEFT JOIN 
	employees1 m
ON
	e.manager_id  = m.id 
GROUP BY
	d.name
ORDER BY
	'Total Salary' DESC;
GO
-- Each employee that lives in a given state (The state can be hard coded for now)
SELECT
	a.state AS 'State',
	COUNT(*) 'Total Employees'
FROM
	addresses1 a
LEFT JOIN
	employees1 e
ON
	a.id = e.address_id
GROUP BY
	a.state
;
GO	
	
	
	

