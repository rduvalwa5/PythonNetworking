'''
Created on Nov 27, 2018

http://www.bitforestinfo.com/2018/01/code-to-ping-request-using-raw-python.html
'''

import subprocess

hostList = ["50.125.93.15","Wireless_Broadband_Router.","192.168.1.1","OsxAir.home", "C1246895-OSX.home","C1246895-OSX2.home","Jacquelyns-iMac.home","BriaMacBookPro.home","c1246895-dell.home","RDuval-XPS.home"]

#host = "OsxAir.home"

for host in hostList:
    ping = subprocess.Popen(
        ["ping", "-c", "1", host],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
        )
    out, error = ping.communicate()
    print (out)
print("Complete ping for ", hostList)