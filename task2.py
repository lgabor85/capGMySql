import os
import mysql.connector
from tabulate import tabulate

# Read the environment variables
db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

# Establish a connection to the MySQL database
conn = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)

# Write an SQL query to print all details of employees, excluding those with first names “Gerard” and “Mary” and save the output in tabular format in a file "employee_details.txt".
file = open('employee_detail.txt', 'w')
cursor = conn.cursor()
cursor.execute("SELECT * FROM employees WHERE firstName NOT IN ('Gerard', 'Mary')")
result = cursor.fetchall()
file.write(tabulate(result, headers=['employeeNumber', 'lastName', 'firstName', 'extension', 'email', 'officeCode', 'reportsTo', 'jobTitle'], tablefmt='grid'))
file.close()

# Close the cursor and connection
cursor.close()
conn.close()