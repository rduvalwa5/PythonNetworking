'''
Created on Nov 26, 2018
https://docs.python.org/3.0/library/ssl.html
@author: rduvalwa2

OSXAir:src rduvalwa2$ ls
Asyncio                echo_client.py            simpleServer.py
PyNet                echo_server.py            windows_sniffer_example.py
PyProgramming_Chap5        simpleClient.py
OSXAir:src rduvalwa2$ sudo python windows_sniffer_example.py
Password:
Traceback (most recent call last):
  File "windows_sniffer_example.py", line 23, in <module>
    s.ioctl(socket.SIO_RCVALL,socket.RCVALL_ON)
AttributeError: '_socketobject' object has no attribute 'ioctl'
OSXAir:src rduvalwa2$ 

'''

import socket

# the public network interface
HOST = socket.gethostbyname(socket.gethostname())

# create a raw socket and bind it to the public interface
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
s.bind((HOST, 0))

# Include IP headers
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# receive all packages
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

# receive a package
print(s.recvfrom(65565))

# disabled promiscuous mode
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)