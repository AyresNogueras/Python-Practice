# Import the socket module to make use of its functions
import socket

# Ask the user to enter the IP address to scan and the range of ports to scan
target = input('Enter the IP address to scan: ')
port_range = input('Enter the range of ports to scan (e.g. 1-100): ')

# Split the start and end port numbers
start_port, end_port = port_range.split('-')

# Create an empty list to store the open ports
open_ports = []

# Print the details of the scan
print('Scanning host', target, 'from port', start_port, 'to port', end_port)

# Loop through each port in the range specified by the user
for port in range(int(start_port), int(end_port) + 1):
    # Create a new socket object using the IPv4 protocol and TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Set a timeout of 0.5 seconds for each connection attempt
    s.settimeout(0.5)
    try:
        # Attempt to connect to the target IP address and port number
        s.connect((target, port))
        # If the connection is successful, add the port number to the list of open ports
        open_ports.append(port)
        # Close the socket
        s.close()
    except:
        # If the connection attempt fails, do nothing and move on to the next port
        pass

# Print the list of open ports
print('Open ports:', open_ports)
