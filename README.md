# python_mysql_nmap


This script allows for multiple ports insertion and also shows the remaining time in hours (decimal) for each line written.
It starts by taking input from the user for the subnet, port(s), and protocol to scan. It then establishes a connection to the MySQL database using the provided credentials and creates a table if it does not already exist.
The script then generates a list of IP addresses from the provided subnet and initializes an instance of the Nmap PortScanner. It calculates the total number of hosts and ports to scan and starts scanning each IP address for each specified port.
For each scan, the script inserts the results into the database with a timestamp, subnet, port number, protocol, IP address, and port status. It then calculates the time elapsed since the script started and estimates the remaining time using the total number of hosts, ports, and the current progress. The remaining time is then printed to the console in hours (decimal) format along with the number of rows inserted, IP address, and port number.
Finally, the script closes the database connection and terminates.
