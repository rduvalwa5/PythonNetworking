'''
Created on Aug 26, 2016
Example from Python Programming Chapter 5
@author: rduvalwa2
'''

import os

# global childPids
childPids = []

def child():
    print('Hello from child', os.getpid())
    os._exit(0) # else goes back to parent loop

def parent():

    while True:
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            print('Hello from parent', os.getpid(), newpid)
            childPids.append(newpid)
            print('parent',childPids)            
        if input() == 'q': 
            print('Child PIDS', childPids)
            break
    
parent()