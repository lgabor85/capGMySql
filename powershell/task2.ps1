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
$query = "SELECT * FROM employees WHERE firstName NOT IN ('Gerard', 'Mary')"

# Execute the query and fetch the results
$result = Invoke-MySQL -Connection $conn -Query $query

# Convert the results to a table format
$results = $result | Format-Table -AutoSize | Out-String

# Write the results to a file
$outfile = "employee_detail.txt"
$results | Out-File -FilePath $outfile

# Close the connection
Disconnect-MySQL -Connection $conn