"""
PYMIN - Make easy
"""

#Import moduls
import os
import time
from adminlinux import menu_admin_linux
from apache import menu_apache
from menu_ssh import menu_ssh
from menu_pla_dhcp import menu_dhcp

def pymin_menu(): 
    while True:
        print ("\nWELCOME TO PYMIN\n")
        print ("\t1.- Manage users and groups")
        print ("\t2.- Web - Apache ")
        print ("\t3.- SSH ")
        print ("\t4.- DHCP ")
        print ("\t5.- Exit")
        
        # Menu options condition
        opcionMenu = input("\nSelect any option: ")
    
        if opcionMenu == "1":
            menu_admin_linux()
            
        elif opcionMenu == "2":
            menu_apache()
            
        elif opcionMenu == "3":
            menu_ssh()
            
        elif opcionMenu == "4":
            menu_dhcp()
           
        #Exit with this while loop using break 
        elif opcionMenu == "5":
            print("\nBye :)")
            break

        else:
            print ("")
            input("Please select the correct option...\npress any key to continue")

pymin_menu()
