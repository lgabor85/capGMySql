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

# Write an SQL query to print “productName” from “products” table next  to  the corresponding “textDescription” 
# with alias “productLine” from the “productlines” table 
# order by “productLine” Ascending and “productName” Descending and save the result in a file named “unique_product.txt”
file = open('unique_product.txt', 'w')
cursor = conn.cursor()
cursor.execute("SELECT p.productName, pl.textDescription AS productLine FROM products p JOIN productlines pl ON p.productLine = pl.productLine ORDER BY pl.textDescription ASC, p.productName DESC;")
result = cursor.fetchall()
file.write(tabulate(result, headers=['productName', 'productLine'], tablefmt='grid'))
file.close()

# Close the cursor and connection
cursor.close()
conn.close()