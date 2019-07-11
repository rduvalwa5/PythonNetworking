''''
Created on Jul 1, 2019
@author: rduvalwa2

Fabric2 appears to only work with Python 2.7
    1.  install python-2.7.16-macosx10.9.pkg
    2.  http://docs.fabfile.org/en/2.4/getting-started.html

C1246895-OSX:~ rduvalwa2$ pip install fabric2
Collecting fabric2
  Downloading https://files.pythonhosted.org/packages/5f/fa/8351bcf31eab4d708347ffaf350f8d1636ef12a736b1a15a7af7075142a4/fabric2-2.4.0-py2.py3-none-any.whl (51kB)
    100% |████████████████████████████████| 61kB 2.0MB/s 
Collecting paramiko>=2.4 (from fabric2)
  Using cached https://files.pythonhosted.org/packages/4b/80/74dace9e48b0ef923633dfb5e48798f58a168e4734bca8ecfaf839ba051a/paramiko-2.6.0-py2.py3-none-any.whl
Collecting invoke<2.0,>=1.1 (from fabric2)
  Downloading https://files.pythonhosted.org/packages/a6/32/6ed0bace971c5310d923e7c4abf475451ef20fa22c458138dd1aad664044/invoke-1.2.0-py2-none-any.whl (206kB)
    100% |████████████████████████████████| 215kB 2.4MB/s 
Collecting cryptography>=1.1 (from fabric2)
  Downloading https://files.pythonhosted.org/packages/e2/bf/3b641820c561aedde134e88528ba68dffe41ed238899fab7f7ef20118aaf/cryptography-2.7-cp27-cp27m-macosx_10_6_intel.whl (1.6MB)
    100% |████████████████████████████████| 1.6MB 1.7MB/s 
Collecting pynacl>=1.0.1 (from paramiko>=2.4->fabric2)
  Downloading https://files.pythonhosted.org/packages/51/83/2db5b919bf9848fe25d301225a16faabc378419e7eaf00da0b7d200fe801/PyNaCl-1.3.0-cp27-cp27m-macosx_10_6_intel.whl (283kB)
    100% |████████████████████████████████| 286kB 3.6MB/s 
Collecting bcrypt>=3.1.3 (from paramiko>=2.4->fabric2)
  Downloading https://files.pythonhosted.org/packages/a0/dc/9810f8233a1263b11f2f6839f1840cc01a7c0c5d0d5e6cabbe270ddca4d3/bcrypt-3.1.7-cp27-cp27m-macosx_10_6_intel.whl (53kB)
    100% |████████████████████████████████| 61kB 2.3MB/s 
Collecting enum34; python_version < "3" (from cryptography>=1.1->fabric2)
  Downloading https://files.pythonhosted.org/packages/c5/db/e56e6b4bbac7c4a06de1c50de6fe1ef3810018ae11732a50f15f62c7d050/enum34-1.1.6-py2-none-any.whl
Collecting asn1crypto>=0.21.0 (from cryptography>=1.1->fabric2)
  Using cached https://files.pythonhosted.org/packages/ea/cd/35485615f45f30a510576f1a56d1e0a7ad7bd8ab5ed7cdc600ef7cd06222/asn1crypto-0.24.0-py2.py3-none-any.whl
Collecting cffi!=1.11.3,>=1.8 (from cryptography>=1.1->fabric2)
  Downloading https://files.pythonhosted.org/packages/16/f6/46a3dece43541b2cbf3776ec2299e370a2408d9380958401cacb6d101853/cffi-1.12.3-cp27-cp27m-macosx_10_6_intel.whl (245kB)
    100% |████████████████████████████████| 256kB 2.3MB/s 
Collecting six>=1.4.1 (from cryptography>=1.1->fabric2)
  Using cached https://files.pythonhosted.org/packages/73/fb/00a976f728d0d1fecfe898238ce23f502a721c0ac0ecfedb80e0d88c64e9/six-1.12.0-py2.py3-none-any.whl
Collecting ipaddress; python_version < "3" (from cryptography>=1.1->fabric2)
  Downloading https://files.pythonhosted.org/packages/fc/d0/7fc3a811e011d4b388be48a0e381db8d990042df54aa4ef4599a31d39853/ipaddress-1.0.22-py2.py3-none-any.whl
Collecting pycparser (from cffi!=1.11.3,>=1.8->cryptography>=1.1->fabric2)
  Using cached https://files.pythonhosted.org/packages/68/9e/49196946aee219aead1290e00d1e7fdeab8567783e83e1b9ab5585e6206a/pycparser-2.19.tar.gz
Installing collected packages: six, pycparser, cffi, pynacl, enum34, asn1crypto, ipaddress, cryptography, bcrypt, paramiko, invoke, fabric2
  Running setup.py install for pycparser ... done
  The scripts inv and invoke are installed in '/Library/Frameworks/Python.framework/Versions/2.7/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  The script fab2 is installed in '/Library/Frameworks/Python.framework/Versions/2.7/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed asn1crypto-0.24.0 bcrypt-3.1.7 cffi-1.12.3 cryptography-2.7 enum34-1.1.6 fabric2-2.4.0 invoke-1.2.0 ipaddress-1.0.22 paramiko-2.6.0 pycparser-2.19 pynacl-1.3.0 six-1.12.0
C1246895-OSX:~ rduvalwa2$ 




'''

from fabric2 import Connection
con = Connection(host = 'C1246895-OSX',user = 'rduvalwa2')
print(con)
#print(con.run('uname -s'))
#msg = "Ran {0.command!r} on {0.connection.host}, got stdout:\n{0.stdout}"
#print(msg.format(result))