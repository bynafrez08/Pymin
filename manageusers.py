import os, time
import sys
import crypt
import bcrypt
import subprocess
import getpass

#shows users home directories
def show_home_directories():
    print("This is all the users home directories: \n")
    list_home = os.listdir("/home")#use os.listdir function to list the content in particular directory.
    print (list_home)

#list all users
def list_all_users():
    os.system("")

#list groups
def list_groups():
    print("")

#create a user.
def create_user():
    username = input("Put the name of the user that you want to create: ")
    password = getpass.getpass("Password for the user: ")
    encrypass = bcrypt.hashpw(password, bcrypt.gensalt())
    os.system("useradd -p "+encrypass+" "+username+"")

#delete user
def user_del():
    deleteusername = input("Put the name of the user that you want to delete: ")
    print("deleting the user...")
    os.system("userdel "+deleteusername+"")
    time.sleep(2)
    print("user deleted successfully...")

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
    #if(deletegroupname == sys.stderr):
    #    print("Sry Group doesn't exits")
    #else:
    #    print("Group deleted successfully...")

#add users in a group
def add_user_in_group():
    usernametoadd = input("Username to add a group: ")
    groupname = input("Group name to add: ")
    print("Adding the user "+usernametoadd+" in a group "+groupname+"...")
    time.sleep(2)
    os.system("usermod -aG "+groupname+" "+usernametoadd+"")
    #if usernametoadd == 2:
    #    print("Error...User doesn't exits")
    #elif groupname == 2:
    #    print("Error...Group doesn't exist")

#remove user in a group
def remove_user_group():
    userremove = input("Username to remove: ")
    groupname = input("Group name to remove user: ")
    time.sleep(2)
    os.system("gpasswd -d "+userremove+" "+groupname+"")

#change users shells
def change_user_shell():
    username = input("Username to change a shell: ")
    shells = input("What type of shell do you want for the user "+username+": ")
    time.sleep(2)
    os.system("usermod "+username+" -s /bin/{0}".format(shells))

#change users permissions
#def change_user_permissions():


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

        elif option == "2":
            ()

        elif option == "3":
            ()

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

        elif option == "11":
            print("\nBye :)")
            os.system('clear')
            break
        
        else:
            print ("")
            input("Please choose the correct option...\npress any key to continue")