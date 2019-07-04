'''
Created on Jul 1, 2019
https://www.tutorialspoint.com/python/python_ssh.htm
SSH or Secure Socket Shell, is a network protocol that provides a secure way to access a remote computer. 
Secure Shell provides strong authentication and secure encrypted data communications between two computers 
connecting over an insecure network such as the Internet. SSH is widely used by network administrators for 
managing systems and applications remotely, allowing them to log in to another computer over a network, 
execute commands and move files from one computer to another.

AS cloud servers become more affordable, SSH is the most commonly used tool to perform various tasks on cloud server. 
We need it for &;minus

Setup a web server for a client's website
Deploy source code to a production server
In python SSH is implemented by using the python library called fabric. It can be used to issue commands remotely 
over SSH.
@author: rduvalwa2

https://packaging.python.org/tutorials/installing-packages/


'''

from fabric import *
# result = Connection('xyz.com').run('uname -s')
msg = "Ran {.command!r} on {.connection.host}, got stdout:\n{.stdout}"
# print(msg.format(result))