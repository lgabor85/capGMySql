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

# 1. Write  an  SQL  query  to  print  all  details  of  all  employees  located  in  offices  within territory “EMEA”. Save the rsults in a file named emea_employees.txt
file = open('emea_employees.txt', 'w')
cursor = conn.cursor()
cursor.execute("SELECT e.* FROM employees e JOIN offices o ON e.officeCode = o.officeCode WHERE o.territory = 'EMEA';")
result = cursor.fetchall()
file.write(tabulate(result, headers=['employeeNumber', 'lastName', 'firstName', 'extension', 'email', 'officeCode', 'reportsTo', 'jobTitle'], tablefmt='grid'))
file.close()

# Close the cursor and connection
cursor.close()
conn.close()