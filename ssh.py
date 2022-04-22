#!/usr/bin/python

import os
import time, subprocess
from termcolor import colored

#check if it's install it the ssh service
def installation_status():
    os.system("apt list | grep openssh-server")

#install ssh if you don't have install it 
def install_ssh():
    os.system("sudo apt -y install openssh-server")

#check ssh service status
def service_status():
    stat = subprocess.call(["systemctl", "is-active", "--quiet", "ssh"])
    if(stat == 0):# if 0 (active), print "Active"
        print("ssh -> is running")
    else:
        print("ssh -> is NOT running")
        statuscommand = input("Dou you want to check more datail why it not running?[y/n]: ")
        if(statuscommand == "y"):
            print(colored("Press Q to exit", 'red'))
            os.system("service ssh status")
    
#stop, restart, status, start openssh server
def change_service_status():

    estat = input("\nstart / stop / restart :")
    
    if estat == "start":
        
        print("Starting the dhcp service...\n")
    
        os.system("sudo service ssh start")
        
        time.sleep(2)

        print("ssh service start successfully\n")
                
    elif estat == "stop":
                        
        print("Stopping the service...\n")

        os.system("sudo service ssh stop")
    
        time.sleep(2)

        print("ssh service successfully stopped\n")

    elif estat == "restart":
        
        print("Restarting the service..\n")

        os.system("sudo service ssh restart")
    
        time.sleep(2)

        print("ssh service restarted successfully\n")
    
    else:
        print ("")
        input("Please select the correct option...\npress any key to continue")

# access to the particular server or host with ssh connection.
def access_host_server():
    username = input("Put the username that you want to access to: ")
    ip = input("Put the Ip address to the destination server or host: ")
    time.sleep(2)
    os.system("ssh " +username+ "@" +ip+"")

#Date that the ssh private key and public key was created, modifiend, etc.
def date_generate_keys():
    print("\nPrivate key date: \n")
    os.system("stat /etc/ssh/ssh_host_rsa_key | awk 'NR==5 || NR==6 || NR==7 || NR==8' | awk '{print $1,$2,$3}' | awk -F'.' '{print $1}'")
    time.sleep(2)
    print("\nPublic key date: \n")
    os.system("stat /etc/ssh/ssh_host_rsa_key.pub | awk 'NR==5 || NR==6 || NR==7 || NR==8' | awk '{print $1,$2,$3}' | awk -F'.' '{print $1}'")

#https://www.tecmint.com/debugfs-command-show-file-creation-time-in-linux/
#Show the actual welcome message ssh connetion.
def print_ssh_welcomemsg():
    print("\nIf you don't have any message set it will don't print anything.\n") 
    time.sleep(3)
    print("Actual ssh welcome message: \n") 
    os.system("cat /etc/motd 2> /dev/null")

#change or set ssh welcome message
def change_ssh_welcomemsg():
    time.sleep(2)
    os.system("touch /etc/motd")
    with open('/etc/motd','w') as f:
        f.write(input("Write the new welcome message: "))
    print("\nThe Actual message: \n")   
    os.system("cat /etc/motd")
    time.sleep(2)
    print("\nMofiying config files...")
    os.system("sed -i -e 's/#PrintLastLog yes/PrintLastLog no/' /etc/ssh/sshd_config")

#Show the dafault ssh port.
def default_port():
    os.system("cat /etc/ssh/sshd_config | grep 'Port' | grep -vE 'GatewayPorts no' | sed 's/[#]//g'")
    #os.system("cat /etc/services | grep 'ssh' | sed -e 's/\<SSH Remote Login Protocol\>//g' | sed 's/[#]//g'") -> i recommend to use this command

#Failed attempts to enter the password 
def print_failed_attempts():
    os.system("cat /etc/ssh/sshd_config | grep 'MaxAuthTries' | sed 's/[#]//g'")

#The known_hosts file lets the client authenticate the server, to check that it isn't connecting to an impersonator. This is for avoid man-in-the-middle attacks. 
#The authorized_keys file lets the server authenticate the user.
#regenerate keys for the server
def regenerate_keys():
    print("\nRegenerating keys for the server... \n")
    os.system("/bin/rm -v /etc/ssh/ssh_host_*")
    time.sleep(2)
    os.system("sudo dpkg-reconfigure openssh-server")
    time.sleep(2)
    print("restarting the service...")
    os.system("sudo service ssh restart")
    print("Remember that if you want to connect to the server on your client machine you need to update the file .ssh/know_hosts")
    time.sleep(3)

#update the file know_hots
def update_known_hosts():
    print("remember if you login with a root user it will update the ssh known_host for that user or if you login with normal user it will update your normal user known_host key.")
    hostname = input("Put the hostname or the IP address: ")
    print("removing the old key from known_hosts...")
    os.system("ssh-keygen -R "+hostname+"")
    time.sleep(2)
    print("Generating the new key...")
    os.system("ssh-keyscan -H "+hostname+" >> ~/.ssh/known_hosts")

#Change the default ssh port.
def change_port():
    print("Checking if there is a comment in the config file...")
    os.system("sed -i '/Port/s/^#//g' /etc/ssh/sshd_config")
    time.sleep(2)
    userportinput = input("Put the actual ssh port number [example: Port 22]: ")
    new_port = input("Set new ssh port [example: Port 20]: ")
    with open("/etc/ssh/sshd.conf", "r") as f:
        text = f.read().replace("{0}".format(userportinput), "{0}".format(new_port)) 
    with open("/etc/ssh/sshd.conf", "w") as w:    
        w.write(text)

def change_password_attempts():
    time.sleep(2)
    os.system("sed -i '/MaxAuthTries/s/^#//g' /etc/ssh/sshd_config") #un-comment the line that contain "MaxAuthTries"  
    usermaxauth = input("Put your actual MaxAuthTries [example: MaxAuthTries 6]: ")  
    userattempts = input("\nNew MaxAuthTries [example: MaxAuthTries 8]: ")
    with open("/etc/ssh/sshd.conf", "r" ) as f:
        text = f.read().replace("{0}".format(usermaxauth),"{0}".format(userattempts)) 
    with open("/etc/ssh/sshd.conf", "w") as w:    
        w.write(text)

#Access with a user without any password in a particular host or server.
def access_without_password():
    print("To access to a particular host or server it will need the public key.\n")
    print("If you dont have any key generated it will create you automatically.\n")
    option = input("If you have already craeted the keys just type 'n' and if it's not just hit ENTER: ")

    username = input("\nPut the username that you want to access without password: ")   
    ip = input("\nDestination IP address[server/host]: ")
    
    if option == "n":
        execute = username
        execute2 = ip
    else:
        print("Generating the private and public key...")
        time.sleep(2)
        os.system("ssh-keygen -t rsa")
        time.sleep(2)
        ex_input = username
        ex_input2 = ip

    #send the public key to the server with ssh-copy-id
    os.system("ssh-copy-id -i ~/.ssh/id_rsa.pub " +username+ "@" +ip+ "")

#MENU

def menu_ssh(): 
    while True:
        time.sleep(2)
        os.system("clear")
        print ("Manage SSH\n")
        print ("\t1.- SSH installation status")
        print ("\t2.- Install SSH ")
        print ("\t3.- SSH Service status ")
        print ("\t4.- Start/Stop/Restart SSH ")
        print ("\t5.- Connect via ssh with a particular host ")
        print ("\t6.- SSH keys modification/creation date ")
        print ("\t7.- Show ssh welcome message ")
        print ("\t8.- Change ssh welcome message ")
        print ("\t9.- Show ssh dafault port ")
        print ("\t10.-Show the failed attempts in ssh login ")
        print ("\t11.- Regenerate the ssh keys to the server ")
        print ("\t12.- Update known_hosts key ")
        print ("\t13.- Change failed attempts in ssh login ")
        print ("\t14.- Access to a particular host without password ")
        print ("\t15.- Exit ")

        optionMenu = input("\nSelect any option: ")
    
        if optionMenu == "1":
            installation_status()

        elif optionMenu == "2":
            install_ssh()

        elif optionMenu == "3":
            service_status()

        elif optionMenu == "4":
            change_service_status()

        elif optionMenu == "5":
            access_host_server()
        
        elif optionMenu == "6":
            date_generate_keys()
            
        elif optionMenu == "7":
            print_ssh_welcomemsg()
            
        elif optionMenu == "8":
            change_ssh_welcomemsg()
           
        elif optionMenu == "9":
            default_port()
            
        elif optionMenu == "10":
            print_failed_attempts()

        elif optionMenu == "11":
            regenerate_keys()
           
        elif optionMenu == "12":
            update_known_hosts()
            
        elif optionMenu == "13":
            change_password_attempts()
        
        elif optionMenu == "14":
            access_without_password()
        
        elif optionMenu == "15":
            print("\nBye :)")
            break
        
        else:
            print ("")
            input("Please select the correct option......\npress any key to continue")
