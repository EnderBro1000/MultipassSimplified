from consolemenu import *
from consolemenu.items import *
from mpsfunc import *
import sys
import getpass
import time
import pretty_errors
import os


# File Wide Variables
app = 'MultipassSimplified'
username = getpass.getuser()
x = f'/home/{username}/snap/multipass'
isFile = os.path.isdir(x) 

#Multipass Install Check
def multipasscheck():
    if isFile: 
        pass
    else: 
        print(f"Please install Multipass before launching {app} ") 
        exit()
       
# Invoking Multipass Check
multipasscheck() 
# GUI Logic 
menu = ConsoleMenu("MultipassSimplified", "A Python TUI Interface for the Multipass VM System by WarpWing")
# Command Logic 
command_item1 = CommandItem("Create New MP Instance", input , ["Enter an input"])
command_item2 = CommandItem("Shell into MP Instance", input , ["Enter an input"])
command_item3 = CommandItem("Start MP Instance", input , ["Enter an input"])
command_item4 = CommandItem("Stop MP Instance", input , ["Enter an input"])
command_item5 = CommandItem("Delete MP Instance", input , ["Enter an input"])
# Menu Append Array
menu.append_item(command_item1)
menu.append_item(command_item2)
menu.append_item(command_item3)
menu.append_item(command_item4)
menu.append_item(command_item5)
# Menu Show Function 
menu.show()
