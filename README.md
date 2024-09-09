# capGMySql

This repository contains a collection of MySQL queries for various tasks, along with automation scripts in PowerShell and Python. It is designed to help users perform common database operations efficiently.

## Installation

To use the queries and scripts in this repository, you need to have the following tools installed on your Linux machine:

- pip
- git
- python3
- powershell7

### Installation Commands

```sh
sudo apt update
sudo apt install -y python3 python3-pip git
sudo snap install powershell --classic

## Usage
**Clone the repository:**
```sh
git clone https://github.com/yourusername/capGMySql.git
cd capGMySql

**Run the SQL queries using the provided PowerShell or Python scripts.**
```sh
python3 task1.py

```powershell
./task1.ps1

## Sample Queries and Automation Scripts
**Task1.ps1**

```sql
SELECT DISTINCT city AS CUSTOMER_CITY
FROM customers;

**Task2.ps1**
```sql
SELECT *
FROM employees
WHERE firstName NOT IN ('Gerard', 'Mary');

**Task3.ps1**
```sql
SELECT CONCAT(firstName, ' ', lastName) AS fullName
FROM employees
WHERE last_name LIKE '%n';

**Task4.ps1**
```sql
SELECT e.*
FROM employees e
JOIN offices o ON e.officeCode = o.officeCode
WHERE o.territory = 'EMEA';

**Task5.ps1**
```sql
SELECT o.territory, COUNT(e.employeeNumber) AS employee_count
FROM employees e
JOIN offices o ON e.officeCode = o.officeCode
GROUP BY o.territory
ORDER BY employee_count DESC;

**Task6.ps1**
```sql
SELECT p.productName, pl.textDescription AS productLine
FROM products p
JOIN productlines pl ON p.productLine = pl.productLine
ORDER BY pl.textDescription ASC, p.productName DESC;

**Task7.ps1**
```sql
SELECT p.productName, SUM(s.quantityOrdered) AS total_quantity_sold
FROM products p
JOIN orderdetails s ON p.productCode = s.productCode
JOIN orders o ON s.orderNumber = o.orderNumber
WHERE o.orderDate BETWEEN '2005-04-01' AND '2005-04-30'
GROUP BY p.productName
ORDER BY total_quantity_sold DESC
LIMIT 5;

**Task8.ps1**
```sql
SELECT p.product_name, 
       COALESCE(SUM(s.quantityOrdered * s.priceEach), 0) AS total_revenue
FROM products p
LEFT JOIN sales s ON p.product_id = s.product_id
GROUP BY p.product_name;