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

#Date that the ssh private key and public key was created, modifiend, etc.
def date_generate_keys():
    print("\nPrivate key generation date: \n")
    os.system("stat /etc/ssh/ssh_host_rsa_key")
    time.sleep(2)
    print("\nPublic key generation date: \n")
    os.system("stat /etc/ssh/ssh_host_rsa_key.pub")


#Show the actual welcome message ssh connetion.

def missatge_benvinguda():
    
    #Avisem al usuari
    print("\nSi no s'ha creat anterioment un missatge de benvinguda per defecte no mostrarà cap\n")
    print("Per crear un missatge de benvinguda selecciona la opció numero 6\n")
    
    time.sleep(3)

    print("Missatge de benvinguda actual: \n")

    #Mostrem en pantalla el missatge actual amb la comanda cat
    os.system("cat /etc/motd")


#MOSTRAR PORT PER DEFECTE SSH.

def port_defecte():

    #Obrim el arxiu sshd_config en mode lectura "r" per guardar
    #la informació d'una linea concreta (14) i mostrar-la
    #en pantalla posterioment.
    f=open("/etc/ssh/sshd_config", "r")
    lines=f.readlines()
    print("\nDefault: \n")
    print (lines[14,15])

#QUANTITAT D'INTENTS ERRONIS PERMESOS SSH.

def intents_erronis():

    #Obrim el arxiu sshd_config en mode lectura "r" per guardar
    #la informació d'una linea concreta (35) i mostrar-la
    #en pantalla posterioment.
    f=open("/etc/ssh/sshd_config", "r")
    lines=f.readlines()
    print("\nNúmero d'intents erronis permesos: \n")
    print (lines[35])


#REGENERAR CLAUS DEL SERVIDOR SSH.

def regenerar_claus():

    #utlitzem comandes del terminal per a esborrar tots els arxius que contingun ssh_host_* 
    #posteriorment utlitzem ssh-keygen per regenerar les claus del servidor.
    #En quan acabi el procés reinicim el servei ssh i recordem al usuari que acutalizi el arxiu 
    #"hosts" del seu pc (~/.ssh/known_hosts)
    
    print("\nRegenerant les claus del servidor... \n")
    
    os.system("/bin/rm -v /etc/ssh/ssh_host_*")
    os.system("sudo dpkg-reconfigure openssh-server")
    os.system("sudo service ssh restart")
    
    print ("\ns'ha completat la regeneració de claus amb éxit, Recorda actualizar l'arxiu ~/.ssh/known_hosts, sino als ordiandors dels ususaris els hi sortirà un missatge d'error al connectar-se!\n")


#CANVIAR MISSATGE DE BENVINGUDA SSH.

def canviar_missatge():

    #Obrim el fitxer /etc/motd en mode "escritura" ("w")
    #Utlitzem un input per a que el usuari escrigui el que vulgui.
    f = open("/etc/motd", "w")
    f.write(input("\nEscriu el nou missatge de benvinguda al teu servidor ssh: \n"))
    f.close()

    #Finalment fem servir la comanda cat per veure el resultat del fitxer modificat
    print("\nMissatge de benvinguda actual: \n")
    os.system("cat /etc/motd")
    print("\n")


#CANVIAR PORT PER DEFECTE SSH.

def canviar_port():

    #Obrim el arxiu sshd_config en mode lecutra "r" per guardar la infomració
    #del contingut del mateix (readlines).
    with open('/etc/ssh/sshd_config', 'r') as f:
        data = f.readlines()

    #Creem una variable amb input per a que el usuari pugui introduïr el port
    #Tambe especifiquem com ho ha d'escriure per evitar confusions.
    nou_port = input("Escull un port (Has d'escriure el següent: \nPort: 20 (o el numero que vulguis): ")
    
    #Finalment sobreescirbim en un linea concreta del fitxer (14)
    #el numero de port que ha escrit el usuari.
    data[14] = nou_port + "\n"
    with open('/etc/ssh/sshd_config', 'w') as f:
        f.writelines(data)
        f.close()
        
      

#CANVIAR LA QUANITAT D'INTENTS ERRONIS PERMESOS SSH.

def canviar_intents():

    #Obrim el arxiu sshd_config en mode lecutra "r" per guardar la infomració
    #del contingut del mateix (readlines).
    with open('/etc/ssh/sshd_config', 'r') as f:
        data = f.readlines()

    #Creem una variable amb input per a que el usuari pugui introduïr el múmero d'intents
    #Tambe especifiquem com ho ha d'escriure per evitar confusions.
    intents = input("Escull el numero d'intents (Has d'escriure el següent: \nMaxAuthTries: 20 (o el numero que vulguis): ")

    #Finalment sobreescirbim en un linea concreta del fitxer (35)
    #el numero de port que ha escrit el usuari.
    data[35] = intents + "\n"
    with open('/etc/ssh/sshd_config', 'w') as f:
        f.writelines(data)
        f.close()


#PERMETRE QUE UN USUSARI ACCEDEIXI AL SERVIDOR SSH SENSE CONTRASENYA.

def accedir_sense_contrasenya():

    print("Per accedir al servidor es necessita una clau publica\n")
    print("Sino la tens aquest programa la genera auotmàticament\n")
    print("Si ja tens una clau publica simplement selecciona la opció n per no sobresciure la clau\n")

    #Generem un parell de claus noves
    os.system("ssh-keygen -t rsa")
    
    #Amb els seguents inputs guardem la informació del ususari
    #i la utlitzem posteriorment per accedir al servidor ssh
    usuari = input("\nNom d'usuari al qual es vol accedir sense contrasenya: ")
    
    lloc = input("\nIp o host del servidor ssh: ")

    print("\n")

    print("Creant directori...\n")
    #Creem un directori .ssh al directori del usuari
    os.system("ssh " + usuari + "@" + lloc + " mkdir -p .ssh")

    print("Copiant clau publica al servidor...\n")
    #Finalment copiem el contingut de la clau pública del pc client al fitxer
    #.ssh/authorized_keys del usuari del servidor.
    os.system("cat .ssh/id_rsa.pub | ssh " + usuari + "@" + lloc + " 'cat >> .ssh/authorized_keys'")

    print("Fet, ja pots accedir sense contrasenya al usuari " + usuari + " del servidor ssh\n")

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
        print ("\t5.- Instal·lar SSH ")
        print ("\t6.- Show ssh welcome message ")
        print ("\t7.- Show default ssh port ")
        print ("\t8.- Show number of failed attempts allowed on ssh connection ")
        print ("\t9.- Regenerate the ssh keys to the server ")
        print ("\t10.- Change ssh welcome message ")
        print ("\t11.- Change default ssh port ")
        print ("\t12.- Change the number of failed attempts allowed on ssh connection ")
        print ("\t13.- Access to the servidor with a specefic user without password ")
        print ("\t14.- Exit")
    
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
            install_ssh()
        
        elif optionMenu == "6":
            missatge_benvinguda()
            
        elif optionMenu == "7":
            port_defecte()
            
        elif optionMenu == "8":
            intents_erronis()
           
        elif optionMenu == "9":
            regenerar_claus()
            
        elif optionMenu == "10":
            canviar_missatge()

        elif optionMenu == "11":
            canviar_port()
           
        elif optionMenu == "12":
            canviar_intents()
            
        elif optionMenu == "13":
            accedir_sense_contrasenya()
        
        elif optionMenu == "14":
            print("\nBye :)")
            break
        
        else:
            print ("")
            input("Please select the correct option......\npress any key to continue")
