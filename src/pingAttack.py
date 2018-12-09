'''
Created on Nov 28, 2018

@author: rduvalwa2
'''

import subprocess

host = "192.168.1.16"

for i in range(100000):
    ping = subprocess.Popen(
        ["ping", "-c", "1", host],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
        )
    out, error = ping.communicate()
    print (out)
print("Complete ping for ", host)