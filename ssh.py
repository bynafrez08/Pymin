#!/usr/bin/env python

#importem tots els moduls necessaris
import os
import time

#VEURE SI SSH ESTA INSTAL·LAT

#Utlitzem la seguent comandna per comprovar si dhcp esta instal·lat
def veure_ssh():
    
    os.system("apt list | grep openssh-server")

        

#ESTAT DEL SERVEI

def estat_serveri_ssh():
    os.system("sudo service ssh status")

#CANVI D'ESTAT

def canviar_estat_ssh():

    estat = input("\nEngegar / Apagar / Reiniciar :")
    
    if estat == "Engegar":
        
        print("Engegant el servei...\n")
    
        os.system("sudo service ssh start")
        
        time.sleep(2)

        print("Servei ssh engegat\n")
                
    elif estat == "Apagar":
                        
        print("Aturant el servidor...\n")

        os.system("sudo service ssh stop")
    
        time.sleep(2)

        print("Servidor ssh aturat\n")

    elif estat == "Reiniciar":
        
        print("Reinicant el servei..\n")

        os.system("sudo service ssh restart")
    
        time.sleep(2)

        print("Servei ssh engegat\n")
    
    else:
        print ("")
        input("No has sleccionat ninguna opció correcta...\nprem qualsevol tecla per continuar")

#INSTAL·LAR DHCP

#utlitzem os.system per executar una comanda al terminal de linux.
def install_ssh():
    os.system("sudo apt -y install ssh ")

#ULTIMA DATA DE GENERACIÓ DE CLAUS DEL SERVIDOR SSH.

#Definim una funció per a cada programa, de tal manera que
#posteriorment els utilitzarem en un menu
def data_generacio_claus():

    #importem els moduls necessaris
    import os

    #Executem la comanda stat que ens mostra, entre d'altres, l'útima data de modificació
    print("\nClau Privada: \n")
    os.system("stat /etc/ssh/ssh_host_rsa_key")

    time.sleep(5)

    print("\nClau Pública: \n")
    os.system("stat /etc/ssh/ssh_host_rsa_key.pub")

    time.sleep(2)

#MOSTRAR MISSATGE DE BENVINGUDA SSH.


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
    print("\nPort per defecte: \n")
    print (lines[14])

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
    
    #afegim un bluce while per a que sempre es repeteixi el menu 
    while True:
    
        #simplement esperem 2 segons per donar temps a llegir els resultats
        time.sleep(5)

        #executem la comanda clear per a fer mes agradable l'execució del menu
        os.system("clear")
    
        #Fem una serie de prints per a que el usuari pugui veurels 
        #i seleccionar una de les opcions
        print ("Manage SSH\n")
        print ("\t1.- Mostrar Última data de generació de claus del servidor ssh")
        print ("\t2.- Comprovar si SSH esta instal·lat ")
        print ("\t3.- Estat del servei SSH ")
        print ("\t4.- Engegar/Apagar/Reinicar SSH ")
        print ("\t5.- Instal·lar SSH ")
        print ("\t6.- Mostrar missatge benvinguda servidor ssh ")
        print ("\t7.- Mostrar port per defecte ssh ")
        print ("\t8.- Mostrar quanitat d'intents erronis permesos ")
        print ("\t9.- Regenerar les claus del servidor ssh ")
        print ("\t10.- Canviar missatge de benvinguda ssh ")
        print ("\t11.- Canviar port per defecte ssh")
        print ("\t12.- Canviar la quanitat d'intents erronis permesos ssh")
        print ("\t13.- Permetre que un ususari pugui accedir al servidor ssh sense contrasenya")
        print ("\t14.- Sortir")
    
        # sol·licitem una opcio al usuari
        opcionMenu = input("\nSelecciona una opció: ")
        
        #ara creem els valors per tal de que si escolleix una
        #de les opcions el porti al programa adient
        if opcionMenu == "1":
            data_generacio_claus()
            
        elif opcionMenu == "2":
            veure_ssh()

        elif opcionMenu == "3":
            estat_serveri_ssh()

        elif opcionMenu == "4":
            canviar_estat_ssh()

        elif opcionMenu == "5":
            install_ssh()
        
        elif opcionMenu == "6":
            missatge_benvinguda()
            
        elif opcionMenu == "7":
            port_defecte()
            
        elif opcionMenu == "8":
            intents_erronis()
           
        elif opcionMenu == "9":
            regenerar_claus()
            
        elif opcionMenu == "10":
            canviar_missatge()

        elif opcionMenu == "11":
            canviar_port()
           
        elif opcionMenu == "12":
            canviar_intents()
            
        elif opcionMenu == "13":
            accedir_sense_contrasenya()
        
        #en la ultima opció afegim un break per poder sortir del bucle
        #i tornar al menu principal   
        elif opcionMenu == "14":
            print("\nADEU :)")
            break

        #Finalment fem servir else per si escolleixen una opció inexistent.
        else:
            print ("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
