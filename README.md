# python_mysql_nmap

This script is a network scanning tool that allows users to scan a range of IP addresses for open ports using Nmap, and then store the results in a MySQL database. It has been designed to be user-friendly, prompting the user to enter the subnet, port number(s), and protocol they want to scan. The script then automatically determines the scan type based on the protocol entered, either TCP or UDP.

The script uses Python libraries to create a connection to a MySQL database and create a table to store the scan results. It then iterates over the IP addresses in the provided subnet and for each IP address, scans the specified port(s) using Nmap. The results are then inserted into the MySQL table.

To provide the user with an estimate of the remaining time for the scan to complete, the script calculates the total number of hosts and ports to scan and uses this to estimate the remaining time for each scan iteration. The script displays this remaining time for each iteration in hours and as a decimal number.

Overall, the script is a useful and user-friendly tool for network administrators and security professionals who want to quickly and easily scan a range of IP addresses for open ports and store the results in a database.




This script allows for multiple ports insertion and also shows the remaining time in hours (decimal) for each line written.
It starts by taking input from the user for the subnet, port(s), and protocol to scan. It then establishes a connection to the MySQL database using the provided credentials and creates a table if it does not already exist.
The script then generates a list of IP addresses from the provided subnet and initializes an instance of the Nmap PortScanner. It calculates the total number of hosts and ports to scan and starts scanning each IP address for each specified port.
For each scan, the script inserts the results into the database with a timestamp, subnet, port number, protocol, IP address, and port status. It then calculates the time elapsed since the script started and estimates the remaining time using the total number of hosts, ports, and the current progress. The remaining time is then printed to the console in hours (decimal) format along with the number of rows inserted, IP address, and port number.
Finally, the script closes the database connection and terminates.
