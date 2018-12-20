'''
Created on Dec 19, 2018
https://docs.python.org/3/library/ipaddress.html?highlight=string
@author: rduvalwa2

https://www.networkworld.com/article/3254575/lan-wan/what-is-ipv6-and-why-aren-t-we-there-yet.html
https://www.internetsociety.org/deploy360/ipv6/
https://en.wikipedia.org/wiki/IPv6_address

IPv6 addresses are 128-bit identifiers for interfaces and sets of interfaces (RFC 4291). In its full notation, 
an IPv6 address is represented in eight groups of four hexadecimal digits (eight 16-bit blocks) separated by colons (:), 
for example
2001:0db8:0a0b:12f0:0000:0000:0000:0001

RFC 5952 recommends to use the compressed format for IPv6 address textual representation:

2001:db8:a0b:12f0::1

Leading zeros MUST be suppressed.
For example, 2001:0db8::0001 is not acceptable and must be represented as 2001:db8::1 
The use of the symbol "::" MUST be used to its maximum capability.
For example, 2001:db8:0:0:0:0:2:1 must be shortened to 2001:db8::2:1. 
The symbol "::" MUST NOT be used to shorten just one 16-bit 0 field.
For example, the representation 2001:db8:0:1:1:1:1:1 is correct, but 2001:db8::1:1:1:1:1 is not correct. 
The characters "a", "b", "c", "d", "e", and "f" in an IPv6 address MUST be represented in lowercase.
'''
import ipaddress

'''
ipaddress.ip_address(address)
Return an IPv4Address or IPv6Address object depending on the IP address passed as argument. 
Either IPv4 or IPv6 addresses may be supplied; integers less than 2**32 will be considered to be IPv4 by default. 
A ValueError is raised if address does not represent a valid IPv4 or IPv6 address.
'''
validIpAdd = '192.168.1.1'
inValidIpAdd = '192.168.1.256'

print(ipaddress.ip_address(validIpAdd))
try:
    print(ipaddress.ip_address(inValidIpAdd))
except ValueError:
    print("ValueError: '", inValidIpAdd ,"' does not appear to be an IPv4 or IPv6 address")
    
print(ipaddress.ip_address("2001:0db8:0a0b:12f0:0000:0000:0000:0001"))   
print(ipaddress.ip_address("2001:db8:0:0:0:0:2:1"))    
print(ipaddress.ip_address("2001:db8:0:1:1:1:1:1"))
try:
    print(ipaddress.ip_address("2001:DB8:::1:1:1:1:1"))
except ValueError:
    print("ValueError: '2001:DB8:::1:1:1:1:1' does not appear to be an IPv4 or IPv6 address")
    
    
'''
ipaddress.ip_network(address, strict=True)
Return an IPv4Network or IPv6Network object depending on the IP address passed as argument. address is a string or integer 
representing the IP network. Either IPv4 or IPv6 networks may be supplied; integers less than 2**32 will be considered 
to be IPv4 by default. strict is passed to IPv4Network or IPv6Network constructor. 
A ValueError is raised if address does not represent a valid IPv4 or IPv6 address, or if the network has host bits set.
'''
print(ipaddress.ip_network('192.168.0.0/13'))
try:
    print(ipaddress.ip_network('192.168.0.1/13'))
except ValueError:
    print("return IPv4Network(address, strict) File \"/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/ipaddress.py\", line 1536, in __init__ /raise ValueError('%s has host bits set' % self)")
    
'''
IP Addresses
Address objects
The IPv4Address and IPv6Address objects share a lot of common attributes. Some attributes that are only meaningful 
for IPv6 addresses are also implemented by IPv4Address objects, in order to make it easier to write code that handles 
both IP versions correctly. Address objects are hashable, so they can be used as keys in dictionaries.
class ipaddress.IPv4Address(address)¶
Construct an IPv4 address. An AddressValueError is raised if address is not a valid IPv4 address.
The following constitutes a valid IPv4 address:
A string in decimal-dot notation, consisting of four decimal integers in the inclusive range 0–255, separated by dots 
(e.g. 192.168.0.1). Each integer represents an octet (byte) in the address. Leading zeroes are tolerated only for values 
less than 8 (as there is no ambiguity between the decimal and octal interpretations of such strings).
An integer that fits into 32 bits.
An integer packed into a bytes object of length 4 (most significant octet first).
'''    
print(ipaddress.IPv4Address(3232235521))
# IPv4Address('192.168.0.1')
print(ipaddress.IPv4Address(b'\xC0\xA8\x00\x01'))
#IPv4Address('192.168.0.1')