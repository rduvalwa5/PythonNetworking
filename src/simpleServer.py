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

message = b"Socket addresses are represented as follows: \
    A single string is used for the AF_UNIX address family. \
    A pair (host, port) is used for the AF_INET address family, where host is a string representing either a hostname in Internet domain notation  \
    like 'daring.cwi.nl' or an IPv4 address like '100.50.200.5', and port is an integral port number.\
    For AF_INET6 address family, a four-tuple (host, port, flowinfo, scopeid) is used, where flowinfo and scopeid represents sin6_flowinfo and \
    sin6_scope_id member in struct sockaddr_in6 in C. For socket module methods, flowinfo and scopeid can be omitted just for backward compatibility.\
    Note, however, omission of scopeid can cause problems in manipulating scoped IPv6 addresses. Other address families are currently not supported. \
    The address format required by a particular socket object is automatically selected based on the address family specified when the socket object was created.\
\
    For IPv4 addresses, two special forms are accepted instead of a host address: the empty string represents INADDR_ANY, and the string\
     '<broadcast>' represents INADDR_BROADCAST. The behavior is not available for IPv6 for backward compatibility, \
     therefore, you may want to avoid these if you intend to support IPv6 with your Python programs.\
\
    If you use a hostname in the host portion of IPv4/v6 socket address, the program may show a nondeterministic behavior, \
    as Python uses the first address returned from the DNS resolution. The socket address will be resolved differently into \
    an actual IPv4/v6 address, depending on the results from DNS resolution and/or the host configuration. For deterministic behavior \
    use a numeric address in host portion."\
    
sockTimeOut = 60
maxConnections = 5
s = socket.socket()         # Create a socket object
s.settimeout(sockTimeOut)
# Example gethostname()
host =  socket.gethostname() # Get local machine name 

port = 12349                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

print("host is ", host, " port is ", port, " time out is ", s.gettimeout())
print("Socket name is",s.getsockname())

# Example listen()
s.listen(maxConnections)                 # Now wait for client connection.
print("Listening max connections are ", maxConnections)

while True:
    c, addr = s.accept()     # Establish connection with client.
    print ('Got connection from', addr)
#    c.send(b'Thank you for connecting    Thank you for connecting     Thank you for connecting    Thank you for connecting    Thank you for connecting')
    c.send(message)
    c.close()                # Close the connection