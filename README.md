# Python-Practice/Port Scanner
This python program was made as a final project for Intro to Python. I felt it was a good program choice since my focus is in Cybersecurity and Information Assurance. 
Port scanning is widely used as a tool to find weak points in a network and ultimately can be used for good or evil.

# Scope
The program is a simple port scanner that allows the user to enter an IP address and a range of port numbers to scan.

It uses the socket module to create socket objects and attempt to connect to the specified port numbers. If a connection is successful, the port number is added to a list of open ports.

The program attempts to connect to the target IP address and port number using the connect() function. If the connection is successful, the port number is added to the list of open ports. 
The socket is then closed using the close() function.

If the connection attempt fails, the program simply moves on to the next port and does not add it to the list of open ports. Finally, the program prints the list of open ports that were found during the scan.

