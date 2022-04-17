
#!/usr/bin/env python

import os, time
import sys
import subprocess

#shows users home directories
def show_home_directories():
    print("This is all the users home directories: \n")
    os.system("ls /home")#use os.listdir function to list the content in particular directory.

#def list_all_users():


#create a user.
#def create_user(): # more simple way to create user using adduser. If you want you can remove the other function and use this one.
#    username = input("Put the name of the user that you want to create: ")
#    os.system("adduser "+username+"")

def create_user():
    username = input("Put the name of the user that you want to create: ")
    print("creating the user and the working directory...")
    os.system("useradd -m "+username+" "+username+"")
    time.sleep(2)
    print("password required...")
    os.system("passwd "+username+"")
    time.sleep(2)
    print("setting a proper shell...")
    os.system("usermod "+username+" -s /bin/bash")
    print("Done.")
        

#delete user
def user_del():
    deleteusername = input("Put the name of the user that you want to delete: ")
    print("deleting the user...")
    os.system("userdel "+deleteusername+"")
    time.sleep(2)
    os.system("rm -r /home/{0}".format(deleteusername))
       
#create group
def create_group():
    groupname = input("Put the name of the group that you want to create: ")
    time.sleep(2)
    os.system("addgroup "+groupname+"")
    #os.system("groupadd "+groupname+"") -> in the case that your distro don't have addgroup command.

#delete group
def delete_group():
    deletegroupname = input("Put the name of the group that you want to delete: ")
    print("Deleting "+deletegroupname+" group...")
    time.sleep(2)
    os.system("groupdel "+deletegroupname+"")
    
#add users in a group
def add_user_in_group():
    usernametoadd = input("Username to add a group: ")
    groupname = input("Group name to add: ")
    print("Adding the user "+usernametoadd+" in a group "+groupname+"...")
    time.sleep(2)
    command = os.system("usermod -aG "+groupname+" "+usernametoadd+"")

#remove user in a group
def remove_user_group():
    userremove = input("Username to remove: ")
    groupname = input("Group name to remove the user "+userremove+": ")
    time.sleep(2)
    os.system("gpasswd -d "+userremove+" "+groupname+"")
            
#change users shells
def change_user_shell():
    username = input("Username to change a shell: ")
    print("This is the shells that you can use on your system:\n")
    time.sleep(2)
    os.system("chmod +x relevant_scripts/shell.sh")
    os.system("./relevant_scripts/shell.sh")
    shells = input("\nWhat type of shell do you want for the user "+username+"?: ")
    time.sleep(2)
    os.system("usermod "+username+" -s /bin/{0}".format(shells))

#change users passwords.
def change_user_password():
    username = input("Username that you want to change the password: ")
    os.system("passwd "+username+"")



#menu
def menu_manageusers():
    while True:
        #which waits a few seconds to display the output.
        time.sleep(2)
        #execute the command so that the outputs are cleaned and the menu is more pleasant.
        os.system("clear")
        #menu options
        print("Manage Users and Groups\n")
        print("\t1.- View Users Home directory")
        print("\t2.- List all the users")
        print("\t3.- List Groups")
        print("\t4.- Create Users")
        print("\t5.- Delete Users")
        print("\t6.- Create Groups")
        print("\t7.- Delete Groups")
        print("\t8.- Add users in a group")
        print("\t9.- Remove users in a group")
        print("\t10.- Change Users shells")
        print("\t11.- Change Users permissions")
        print("\t12.- Change Users passwords")
        print("\t13.- Exit menu")            
        
        #condition for the menu options.
        option = input("\nSelect Any option: ")
        
        if option == "1":
           show_home_directories() 

        #elif option == "2":
            #list_all_users()

        #elif option == "3":
            #list_groups()

        elif option == "4":
            create_user()

        elif option == "5":
            user_del()

        elif option == "6":
            create_group()
        
        elif option == "7":
            delete_group()
        
        elif option == "8":
            add_user_in_group()

        elif option == "9":
            remove_user_group()
        
        elif option == "10":
            change_user_shell()

        #elif option == "11":
            #change_user_permissions()

        elif option == "12":
            change_user_password()

        elif option == "13":
            print("\nBye :)")
            os.system('clear')
            break
        
        else:
            print ("")
            input("Please choose the correct option...\npress any key to continue")