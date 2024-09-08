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

# Write  an  SQL  query  to  print  full  name  as  concatenation  of  first  and  last  name  of employees whose last name ends with ‘n’. Save the reults in a file named uniqueNames.txt
file = open('unique_names.txt', 'w')
cursor = conn.cursor()
cursor.execute("SELECT CONCAT(firstName, ' ', lastName) AS fullName FROM employees WHERE lastName LIKE '%n'")
result = cursor.fetchall()
file.write(tabulate(result, headers=['fullName'], tablefmt='grid'))
file.close()

# Close the cursor and connection
cursor.close()
conn.close()