'''
Created on Nov 25, 2018

https://www.tutorialspoint.com/python/python_networking.htm

C1246895-osx:src rduvalwa2$ python simpleServer.py 
^CTraceback (most recent call last):
  File "simpleServer.py", line 17, in <module>
    c, addr = s.accept()     # Establish connection with client.
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/socket.py", line 206, in accept
    sock, addr = self._sock.accept()
KeyboardInterrupt
C1246895-osx:src rduvalwa2$ python simpleServer.py 
('Got connection from', ('192.168.1.8', 49559))
('Got connection from', ('192.168.1.8', 49560))

'''
#!/usr/bin/python           # This is server.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = "c1246895-osx2.home"# socket.gethostname() # Get local machine name 
port = 12349                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
    c, addr = s.accept()     # Establish connection with client.
    print ('Got connection from', addr)
    c.send('Thank you for connecting')
    c.close()                # Close the connection