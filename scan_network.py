import csv
import nmap
import mysql.connector
from datetime import datetime
import ipaddress
import time

subnet = input("Enter the subnet (in CIDR notation): ")
port = input("Enter the port number(s), separated by commas: ")
protocol = input("Enter 'tcp' or 'udp' for the protocol to scan: ")
db_host = 'dbhost'
db_user = 'dbuser'
db_pass = 'dbpassF'
db_name = 'dbname'

if protocol.lower() == "tcp":
    scan_type = "sS" # TCP SYN scan
elif protocol.lower() == "udp":
    scan_type = "sU" # UDP scan
else:
    print("Invalid protocol specified.")
    exit(1)

now = datetime.now()
date_time = now.strftime("%Y-%m-%d %H:%M:%S")

db = mysql.connector.connect(
  host=db_host,
  user=db_user,
  password=db_pass,
  database=db_name
)

cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS scan_results (id INT AUTO_INCREMENT PRIMARY KEY, scan_time DATETIME, subnet VARCHAR(255), port INT, protocol VARCHAR(10), ip_address VARCHAR(255), port_status VARCHAR(10))")

ip_list = [str(ip) for ip in ipaddress.IPv4Network(subnet)]

nm = nmap.PortScanner()
total_hosts = len(ip_list)
total_ports = len(port.split(','))
start_time = time.time()

for i, ip_address in enumerate(ip_list):
    for j, port_num in enumerate(port.split(',')):
        nm.scan(ip_address, arguments='{} -p {}'.format(scan_type, port_num))
        try:
            port_status = nm[ip_address]['tcp'][int(port_num)]['state']
        except KeyError:
            port_status = 'unknown'
        sql = "INSERT INTO scan_results (scan_time, subnet, port, protocol, ip_address, port_status) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (date_time, subnet, port_num, protocol, ip_address, port_status)
        cursor.execute(sql, val)
        db.commit()
        time_elapsed = time.time() - start_time
        time_remaining = ((total_hosts * total_ports) - (i * total_ports + j)) * time_elapsed / (i * total_ports + j + 1)
        time_remaining_hours = round(time_remaining / 3600, 2)
        print(cursor.rowcount, "record inserted for host:", ip_address, "on port", port_num, "Remaining time (hours, decimal):", time_remaining_hours)

db.close()
