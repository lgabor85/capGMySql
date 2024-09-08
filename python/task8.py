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

# Write an SQL query to print total revenue along with product names for all products
# and save the result in a file named “total_revenue.txt”
file = open('total_revenue.txt', 'w')
cursor = conn.cursor()
cursor.execute("""
    SELECT p.productName, 
           COALESCE(SUM(s.quantityOrdered * s.priceEach), 0) AS total_revenue
    FROM products p
    LEFT JOIN orderdetails s ON p.productCode = s.productCode
    GROUP BY p.productName;
""")
result = cursor.fetchall()
file.write(tabulate(result, headers=['productName', 'total_revenue'], tablefmt='grid'))
file.close()

# Close the cursor and connection
cursor.close()
conn.close()