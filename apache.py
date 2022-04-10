import os
import sys
import subprocess
import time

#view apache installation status.
def status_installation():
    os.system("dpkg --get-selections | grep apache")

#install apache2
def install_apache():
    os.system("sudo apt-get install apache2")

#show the apache service status.
def apache_status():
    stat = subprocess.call(["systemctl", "is-active", "--quiet", "apache2"])
    if(stat == 0):# if 0 (active), print "Active"
        print("Apache -> is running")
    else:
        print("Apache -> is NOT running")
        moredetail = input("more detail about why is not running?[y/n]: ")
        if(moredetail == "y"):
            os.system("service apache2 status")

#list sites available 
def list_sites():
    print("These are the available sites: \n")
    os.system("ls /etc/apache2/sites-available")
    #listarr = os.listdir("/etc/apache2/sites-available")
    #print (listarr.replace('[', ''))

#list enbled sites
def list_enable():
    print("These are the enabled sites: \n")
    listena = os.listdir("/etc/apache2/sites-enabled")
    print (listena)

#start/stop/restart apache
def change_apache_status():

    estat = input("\nstart / stop / restart :")
    
    if estat == "start":
        
        print("Starting the apache service...\n")
    
        os.system("sudo service apache2 start")
        
        time.sleep(2)

        print("Apache service start successfully\n")
                
    elif estat == "stop":
                        
        print("Stopping the service...\n")

        os.system("sudo service apache2 stop")
    
        time.sleep(2)

        print("Apache service successfully stopped\n")

    elif estat == "restart":
        
        print("Restarting the apache service...\n")

        os.system("sudo service apache2 restart")
    
        time.sleep(2)

        print("Apache service successfully restarted\n")
    
    else:
        print ("")
        input("Please select the correct option...\npress any key to continue")


#enable and disable the apache service.
def ed():
    options = input("Do you want to enable or disable site?[e/d]: ")
    if options == "e":
        option1 = input("Put the domain name to enable: ")
        print("enabling the site...")
        os.system("a2ensite "+option1+" 1> /dev/null")
        time.sleep(2)
        os.system("service apache2 reload")
        print("reloading the site...")

#create sites
def create_sites():
    vhost = input("Put the domain name of your vhost: ")
    cmd = "mkdir /var/www/{0}".format(vhost)#when the virtual host is created, a test page will be created in the var/www route to verify the site is hosted correctly, this part it's not very important.
    os.system(cmd)
    
    #add permissions
    cmd = "chown -R $USER:$USER /var/www/{0}".format(vhost)
    os.system(cmd)
    
    cmd = "chmod -R 755 /var/www/{0}".format(vhost)
    os.system(cmd)
    
    #create an index.html file for that test web page (remember that this is not necessary to do, but it's for check if your vhost is hosting correctly).
    filename = '/var/www/{0}/index.html'.format(vhost)
    f = open(filename, 'w')
    f.write("<html><head><title>MySite</title></head><body><h1>Hi! this a test webpage</h1></body></html>")
    f.close()
    
    #which will contain the conf file of the site that the user has created.
    filename = '/etc/apache2/sites-available/{0}.conf'.format(vhost)
    filecontent = """<VirtualHost *:80>\r\n
                    ServerAdmin webmaster@localhost\r\n
                    ServerName {0}\r\n
                    ServerAlias www.{0}\r\n
                    DocumentRoot /var/www/{0}\r\n
                    ErrorLog /var/log/apache2/error.log\r\n
                    CustomLog /var/log/apache2/access.log combined\r\n
                    </VirtualHost>\r\n""".format(vhost)
    f =  open(filename, 'w')

    f.write(filecontent)
    f.close()
    
    #enable the site the user created.
    print("enabling the site ...\n")
    time.sleep(2)
    os.system("a2ensite {0} 1> /dev/null".format(vhost))
    
    #disable site by default.
    #cmd = "a2dissite 000-default.conf"
    #os.system(cmd)
    
    #check of the config file of your site is OK.
    #cmd = "apache2ctl configtest"
    #os.system(cmd)
    
    #reload apache
    print("reloading the service...\n")
    time.sleep(2)
    os.system("service apache2 reload")

    #restart apache2
    print("restarting the service...\n")
    time.sleep(2)
    os.system("service apache2 restart")
    time.sleep(2)
    print("site created successfully...")

    #in the /etc/hosts file we are going to add the domain name so that when accessing from the browser the virtual hosting applies to us.
    hosts = vhost
    with open("/etc/hosts", "a") as a_file: #remove the "a" in a_file
        a_file.write("\n127.0.0.1\t" + vhost)
        #a_file.write(vhost)


#menu
def menu_apache():
    while True:
        #which waits a few seconds to display the output.
        time.sleep(2)
        #execute the command so that the outputs are cleaned and the menu is more pleasant.
        os.system("clear")
        #menu options
        print("Web - Apache\n")
        print("\t1.- View installation status")
        print("\t2.- Install apache")
        print("\t3.- View service status")
        print("\t4.- Start/Stop/Restart the service")
        print("\t5.- List availabe site")
        print("\t6.- Enable/Disable sites")
        print("\t7.- Create Sites")
        print("\t8.- List enable sites")
        print("\t9.- Exit menu")            
        
        #condition for the menu options.
        option = input("\nSelect Any option: ")
        
        if option == "1":
           status_installation() 

        elif option == "2":
            install_apache()

        elif option == "3":
            apache_status()

        elif option == "4":
            change_apache_status()

        elif option == "5":
            list_sites()

        elif option == "6":
            ed()
        
        elif option == "7":
            create_sites()

        elif option == "8":
            list_enable()

        elif option == "9":
            print("\nBye :)")
            os.system('clear')
            break
        
        else:
            print ("")
            input("Please choose the correct option...\npress any key to continue")