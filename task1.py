import os
import mysql.connector
from tabulate import tabulate

# Step 1: Read the environment variables
db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

# Step 2: Establish a connection to the MySQL database
conn = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)

# Write an SQL query to fetch unique values of “city” from “customers” table using the alias name as “CUSTOMER_CITY” and output the result in a tabular format into a file named “unique_cities.txt”.
file = open('unique_cities.txt', 'w')
cursor = conn.cursor()
cursor.execute('SELECT DISTINCT city AS CUSTOMER_CITY FROM customers')
result = cursor.fetchall()
file.write(tabulate(result, headers=['CUSTOMER_CITY'], tablefmt='grid'))
file.close()

# Close the cursor and connection
cursor.close()
conn.close()