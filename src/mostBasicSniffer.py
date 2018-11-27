'''
Created on Nov 26, 2018

https://www.binarytides.com/python-packet-sniffer-code-linux/

Sniffer info
http://www.bitforestinfo.com/2017/01/how-to-write-simple-packet-sniffer.html
'''
#Packet sniffer in python
#For Linux

import socket

#create an INET, raw socket
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

# receive a packet
while True:
    print (s.recvfrom(65565))