from consolemenu import *
from consolemenu.items import *
import sys
import getpass
import time
import pretty_errors
import os

# MPS Console Logic 
def mainconsole(): 
    g = input('Enter your input: ')
    f = int(g)
    if f == 1:
        print("Launch Instance with Parameters")
    elif f == 2: 
        print("Stop Instance with Parameters")
    elif f == 3:
        print("Delete Instance with Parameters")
    elif f == 4: 
        pass
    elif f == 5:
        pass
    elif f == 6:
        pass
    elif f == 7:
        pass
    elif f == 8:
        pass
    elif f == 9:   
        pass  
    else:
        print("Invalid Operation!")


def warpwing():
    print("Function Test")
    time.sleep(6)
warpwing()