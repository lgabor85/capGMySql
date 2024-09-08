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

# Write  an  SQL  query  to  fetch  the  no.  of  employees  for  each  territory.  
# Sort  by  no.  of employees in the descending order and save the results in a file named emea_employee_count.txt
file = open('emea_employee_count.txt', 'w')
cursor = conn.cursor()
cursor.execute("SELECT o.territory, COUNT(e.employeeNumber) AS employee_count FROM employees e JOIN offices o ON e.officeCode = o.officeCode GROUP BY o.territory ORDER BY employee_count DESC;")
result = cursor.fetchall()
file.write(tabulate(result, headers=['territory', 'employee_count'], tablefmt='grid'))
file.close()

# Close the cursor and connection
cursor.close()
conn.close()