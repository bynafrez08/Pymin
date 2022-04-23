#!/usr/bin/python

import os
import time
import subprocess
import re
from termcolor import colored 

#Check if the user have install it the dhcp server.
def installation_status():
    os.system("apt list | grep isc-dhcp-server")

#Check the dhcp service status

def service_status():
    #os.system("sudo service isc-dhcp-server status")
    stat = subprocess.call(["systemctl", "is-active", "--quiet", "isc-dhcp-server"])
    if(stat == 0):# if 0 (active), print "Active"
        print("dhcp-server -> is running")
    else:
        print("dhcp-server -> is NOT running")
        statuscommand = input("Dou you want to check more datail why it not running?[y/n]: ")
        if(statuscommand == "y"):
            print(colored("Press Q to exit", 'red'))
            os.system("service isc-dhcp-server status")

#stop, restart, status, start dhcp server

def change_service_status():

    estat = input("\nstart / stop / restart :")
    
    if estat == "start":
        
        print("Starting the dhcp service...\n")
    
        os.system("sudo service isc-dhcp-server start")
        
        time.sleep(2)

        print("Dhcp service start successfully\n")
                
    elif estat == "stop":
                        
        print("Stopping the service...\n")

        os.system("sudo service isc-dhcp-server stop")
    
        time.sleep(2)

        print("dhcp service successfully stopped\n")

    elif estat == "restart":
        
        print("Restarting the service..\n")

        os.system("sudo service isc-dhcp-server restart")
    
        time.sleep(2)

        print("dhcp service restarted successfully\n")
    
    else:
        print ("")
        input("Please select the correct option...\npress any key to continue")

#install dhcp in the case that the user have not installet yet.
def install_dhcp():
    os.system("sudo apt -y install isc-dhcp-server ")

#Check available subnets and hosts
def show_subenet_hosts(): 
    file = open("/etc/dhcp/dhcpd.conf", "r")
    print("\nIf you don't have any subnet or host created it don't output anything\n")
    print("\nActive subnets: \n")
    time.sleep(2)
    os.system("cat /etc/dhcp/dhcpd.conf | grep 'subnet' | grep -v '#' | cut -d' ' -f1,2")
    #os.system("cat /etc/dhcp/dhcpd.conf | grep 'subnet\|range' | grep -v '#'") -> if you want to check the range and the netmask of the subnet.
    print ("\navailable hosts: \n")
    os.system("cat /etc/dhcp/dhcpd.conf | grep 'host' | grep -v '#' | cut -d' ' -f1,2")
    #os.system("cat /etc/dhcp/dhcpd.conf | grep 'host\|hardware\|fixed' | grep -v '#'") -> if you want to check the MAC address and the fixed IP address.

#set MAX_LEASE_TIME

def change_max_lease_time(): 
    output_actual_max =  subprocess.Popen("cat /etc/dhcp/dhcpd.conf | awk '/max-lease-time/{print; exit}'", shell=True, stdout=subprocess.PIPE).stdout
    # awk '/max-lease-time/{print; exit}' | sed -e 's/\<max-lease-time\>//g' | sed 's/[;]//g' -> In the case that you want to just output the seconds.
    output_lease =  output_actual_max.read()
    print("Here is your actual MAX_LEASE_TIME in your system:", output_lease.decode()) 
    #os.system("sed -i '/"+max-lease-time+"/d' /etc/dhcp/dhcpd.conf")
    time.sleep(2)
    putoldmax = input("put your actual MAX-LEASE-TIME (copy and paste it): ")
    new_max = input("Set new max-lease-time (You must type the following): \ max-lease-time 600; (or the number that you want): ") 
    with open("/etc/dhcp/dhcpd.conf", "r") as r:
        text = r.read().replace("{0}".format(putoldmax), "{0}".format(new_max)) 
    with open("/etc/dhcp/dhcpd.conf", "w") as w:
        w.write(text)
    
#DEFAULT_LEASE_TIME

def change_default_lease_time():
    output_actual_max =  subprocess.Popen("cat /etc/dhcp/dhcpd.conf | awk '/default-lease-time/{print; exit}'", shell=True, stdout=subprocess.PIPE).stdout
    output_lease =  output_actual_max.read()
    print("Here is your actual DEFAULT_LEASE_TIME in your system:", output_lease.decode())
    time.sleep(2)
    putoldmax = input("put your actual DEFAULT-LEASE-TIME (copy and paste it): ")
    new_max = input("Set new default-lease-time (You must type the following): \ default-lease-time 600; (or the number that you want): ") 
    with open("/etc/dhcp/dhcpd.conf", "r") as r:
        text = r.read().replace("{0}".format(putoldmax), "{0}".format(new_max)) 
    with open("/etc/dhcp/dhcpd.conf", "w") as w:
        w.write(text)
    
#SUBNET

def create_subnet():
    # User data variables
    subnet = input("Create a subnet: ")
    netmask = input("\nSubnet mask: ")
    ranges = input("\nSet IP ranges (Remember to separate with a space between ip's): ")
    option_routers = input("\noption_routers: ")
    option_domain_name_servers = input("\noption_domain_name_servers (Remember to separate with a comma followed by a space to add more than one server.): ")
    option_domain_name = input("\noption_domain_name (Remember to add ; on the last line on your domain name ""): ") 
    #create a subnet and add on the last line of the file.
    with open('/etc/dhcp/dhcpd.conf', 'a') as f:
        f.write("\n" + "subnet " + subnet + " netmask " + netmask + " {" + "\n" + "    " + "range "
        + ranges + ";" + "\n" + "    " + "option routers " + option_routers + ";" + "\n" + "    " 
        + "option-domain-name-servers " + option_domain_name_servers + ";" + "\n" + "    " 
        + "option-domain-name " + option_domain_name + ";" + "\n  }")
    #restart the dhcp-server once the user set the config.
    os.system("sudo service isc-dhcp-server restart")
    print("\nDone.\n")

#FIXED IP ADDRESSES

def fixed_addresses():
    #User data variables
    host = input("Hostname: ") 
    mac = input("\nMAC Address: ")
    fixed_address = input("\nSet fixed IP address: ") 
    #open the dhcp.conf file and add this informartion to the last line of the file
    with open('/etc/dhcp/dhcpd.conf', 'a') as f:
        f.write("\n" + "host " + host + " {" + "\n" + "    " + "hardware ethernet " + mac + ";"
        + "\n" + "    " + "fixed-address " + fixed_address + ";" + "\n  }")
    #restart the service
    os.system("sudo service isc-dhcp-server restart")
    print("\nDone.\n")

#MENU
def menu_dhcp():
    #create a loop that reapet the menu 
    while True:
        #wait few seconds to output the results.
        time.sleep(3)
        #to clear the menu
        os.system("clear")
        #menu options
        print ("\nDHCP\n")
        print ("\t1.- Install dhcp-server ")
        print ("\t2.- Check if isc-dhcp-server is install it ")
        print ("\t3.- View service status ")
        print ("\t4.- Start/Stop/Restart DHCP ")
        print ("\t5.- Show active subnets and fixed hosts")
        print ("\t6.- Modify the max-lease-time ")
        print ("\t7.- Modify the default-lease-time ")
        print ("\t8.- Create a subnet ")
        print ("\t9.- Create fixed IP addresses ")
        print ("\t10.- Exit")
        # menu conditions 
        optionMenu = input("\nSelect any option: ")
 
        if optionMenu == "1":
            install_dhcp()

        elif optionMenu == "2":
            installation_status()

        elif optionMenu == "3":
            service_status()

        elif optionMenu == "4":
            change_service_status()
            
        elif optionMenu == "5":
            show_subenet_hosts()
            
        elif optionMenu == "6":
            change_max_lease_time()
            
        elif optionMenu == "7":
            change_default_lease_time()
           
        elif optionMenu == "8":
            create_subnet()
            
        elif optionMenu == "9":
            fixed_addresses()

        #and break to exit on the loop    
        elif optionMenu == "10":
            print("\nBye :)")
            time.sleep(2)
            os.system("clear")
            break

        else:
            print ("")
            input("Please select the correct option......\npress any key to continue")
