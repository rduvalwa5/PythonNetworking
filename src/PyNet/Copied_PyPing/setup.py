#!/usr/bin/env python
#-*- encoding: utf-8 -*-
"""
FILE.py
DESC

Copyright (c) 2008 Pierre "delroth" Bourdon <root@delroth.is-a-geek.org>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from distutils.core import setup
from ping import __version__

setup(
    name="ping",
    version=__version__,
    py_modules=[
        'ping'
    ],
    
    author="Pierre Bourdon",
    author_email="delroth@gmail.com",
    description="An implementation of ICMP ping in Python",
    long_description=open('README').read(),
    license="GPL2",
    keywords="ping icmp network latency",
    url="http://bitbucket.org/delroth/python-ping/",
    download_url="http://bitbucket.org/delroth/python-ping/downloads/python-ping-%s.tar.gz" % __version__,
    
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Unix",
        "Programming Language :: Python :: 2",
        "Topic :: Internet",
        "Topic :: Software Developement :: Libraries :: Python Modules",
        "Topic :: System :: Networking",
        "Topic :: System :: Networking :: Monitoring",
    ],
)
