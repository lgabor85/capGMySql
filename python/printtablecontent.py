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

# Step 3: Create a cursor object
cursor = conn.cursor()

# Step 4: List all tables
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

# Open a file for writing
with open('output.txt', 'w') as file:
    # Iterate over each table and fetch its content
    for (table_name,) in tables:
        file.write(f"Contents of table {table_name}:\n")
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        table_output = tabulate(rows, headers=columns, tablefmt="grid")
        file.write(table_output + "\n\n")

# Close the cursor and connection
cursor.close()
conn.close()