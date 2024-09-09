# Load the MySQLCmdlets module
Import-Module MySQLCmdlets

# Read the environment variables
$db_host = $env:DB_HOST
$db_user = $env:DB_USER
$db_password = $env:DB_PASSWORD
$db_name = $env:DB_NAME
$db_port = $env:DB_PORT

# Establish a connection to the MySQL database
$conn = Connect-MySQL -Server $db_host -Database $db_name -User $db_user -Password $db_password -Port $db_port

# Write an SQL query to fetch unique values of “city” from “customers” table using the alias name as “CUSTOMER_CITY” and output the result in a tabular format into a file named “unique_cities.txt”.
$query = "SELECT p.productName, SUM(s.quantityOrdered) AS total_quantity_sold
    FROM products p
    JOIN orderdetails s ON p.productCode = s.productCode
    JOIN orders o ON s.orderNumber = o.orderNumber
    WHERE o.orderDate BETWEEN '2005-04-01' AND '2005-04-30'
    GROUP BY p.productName
    ORDER BY total_quantity_sold DESC
    LIMIT 5;
"

# Execute the query and fetch the results
$result = Invoke-MySQL -Connection $conn -Query $query

# Convert the results to a table format
$results = $result | Format-Table -AutoSize | Out-String

# Write the results to a file
$outfile = "top_products_april_2005.txt"
$results | Out-File -FilePath $outfile

# Close the connection
Disconnect-MySQL -Connection $conn