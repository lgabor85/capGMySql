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

# Write an SQL query to print top 5 products with highest total quantity sold in April, 2005
# and save the result in a file named “top_products_april_2005.txt”
file = open('top_products_april_2005.txt', 'w')
cursor = conn.cursor()
cursor.execute("""
    SELECT p.productName, SUM(s.quantityOrdered) AS total_quantity_sold
    FROM products p
    JOIN orderdetails s ON p.productCode = s.productCode
    JOIN orders o ON s.orderNumber = o.orderNumber
    WHERE o.orderDate BETWEEN '2005-04-01' AND '2005-04-30'
    GROUP BY p.productName
    ORDER BY total_quantity_sold DESC
    LIMIT 5;
""")
result = cursor.fetchall()
file.write(tabulate(result, headers=['productName', 'total_quantity_sold'], tablefmt='grid'))
file.close()

# Close the cursor and connection
cursor.close()
conn.close()