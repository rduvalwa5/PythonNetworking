'''
Created on Nov 25, 2018

https://www.tutorialspoint.com/python/python_networking.htm

OSXAir:src rduvalwa2$ python simpleClient.py 
('connecting to ', 'C1246895-OSX2.home', ' at port', 12349)
Thank you for connecting
OSXAir:src rduvalwa2$ python simpleClient.py 
('connecting to ', 'C1246895-OSX2.home', ' at port', 12349)
Thank you for connecting
OSXAir:src rduvalwa2$ 

'''
#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12349                # Reserve a port for your service.
print("connecting to ", host, " at port" ,port)
s.connect((host, port))
print(s.getsockname(), s.gettimeout())
print (s.recv(1024))
s.close                     # Close the socket when done