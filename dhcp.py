#!/usr/bin/env python

import os
import time
import subprocess
from 

#Check if the user have install it the dhcp server.
def installation_status():
    os.system("apt list | grep isc-dhcp-server")

#Check the dhcp service status

def estat_servei_dhcp():
    os.system("sudo service isc-dhcp-server status")
    time.sleep(5)

#stop, restart, status, start

def canviar_estat_dhcp():

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

#MOSTRAR SITIOS ACTIVOS Y DISPONIBLES
'''def mostrar_llocs():

    #open dhcpd.conf 
    file = open("/etc/dhcp/dhcpd.conf", "r")

    print("\nIf you don't have any subnet or host created it don't output anything\n")
    print("\nLugares disponibles y activos: ")
    
     #Especifiquem las lines que queremos que se muestren en pantalla
     #de forma que se mostrarán los sitios creados ya que lo he programado
     #per a que escriba tanto direcciones fijas como subredes al final del archivo dhcpd.conf
    lines_to_print = [111, 112, 113 ,114, 115, 116 ,117, 118, 119 ,120, 121, 122 ,123, 124, 125 
    ,126, 127, 128 ,129, 130, 131,132, 133, 134 ,135, 136, 137, 138]

    for index, line in enumerate(file):

        if ( index in lines_to_print):

            print(line)

    time.sleep(5)

    file.close()'''


#set MAX_LEASE_TIME

def change_max_lease_time(): 
    output_actual_max =  subprocess.Popen("cat /etc/dhcp/dhcpd.conf | awk '/max-lease-time/{print; exit}' | sed -e 's/\<max-lease-time\>//g' | sed 's/[;]//g'", shell=True, stdout=subprocess.PIPE).stdout
    output_lease =  output_actual_max.read()
    print("Here is your actual MAX_LEASE_TIME in your system:", output_lease.decode())
    
    #quit_max_lease = "max-lease-time"
    #os.system("sed -i '/"+max-lease-time+"/d' /etc/dhcp/dhcpd.conf")
    time.sleep(2)
    new_max = input("Modify max-lease-time (You must type the following): \ max-lease-time 600; (or the number that you want): ")
    filereplace("/etc/dhcp/dhcp.conf", output_actual_max ,"{0}".format(new_max))
    #with open('/etc/dhcp/dhcpd.conf', 'r+') as f:
        

#DEFAULT_LEASE_TIME

def canviar_default_lease_time():

    #obrimos el dhcp.conf y leemos el fichero para guardar su contingut en la variable fecha
    with open('/etc/dhcp/dhcpd.conf', 'r') as f:
        data = f.readlines()

     #Utlitzemos print para mostrar en pantalla cuál es el default_lease actual
     #Asi lo hacemos al especificar el numero de linea dentro del dhcp.conf que queremos mostrar
     #En este caso la fila 12 cuento por defecto el default-lease, y
     #farem servir lo mismo con los otros archivos
    print("default-lease-time actual: \n")
    print(data[12])

    #creem una variable per a que el usuari escrigui el nou valor de default-lease
    nou_default = input("Modifica el default-lease-time (Has d'escriure el següent): \ndefault-lease-time 600; (o el numero que vulguis): ")
    
    #com en el cas anterior obrim el fitxer pero en aquest cas mode escritura
    #escribim la variable introduida per el usuari a la linea 12
    data[12] = nou_default + "\n"
    with open('/etc/dhcp/dhcpd.conf', 'w') as f:
        f.writelines(data)
        f.close()

    with open('/etc/dhcp/dhcpd.conf', 'r') as f:
        data = f.readlines()

    #per acabar tornem a mostrar per pantalla el default-lease actual
    print("\ndefault-lease-time actual: \n")
    print(data[12])
    f.close()



#SUBXARXA

def crear_subxarxa():

    #import els moduls necessaris
    import os
    
    #Primer de tot creem variables per guardar la informació del usuari
    #per poder modificar la configuració de dhcpd
    subnet = input("Subxarxa a crear: ")
    netmask = input("\nMáscara de xarxa: ")
    range = input("\nRang per assginar ip's (Recorda separar amb un espai entre ip's): ")
    option_routers = input("\noption_routers: ")
    option_domain_name_servers = input("\noption_domain_name_servers (Recorda separar amb una coma seguit d'un espai per afegir més d'un servidor.): ")
    option_domain_name = input("\noption_domain_name (Recorda escriure el domini entre cometes ""): ")

    #obrim el ftixer /etc/dhcp/dhcpd.conf en mode "a" per escriure
    #al final del fitxer
    with open('/etc/dhcp/dhcpd.conf', 'a') as f:
        f.write("\n" + "subnet " + subnet + "netmask " + netmask + " {" + "\n" + "    " + "range "
        + range + ";" + "\n" + "    " + "option routers " + option_routers + ";" + "\n" + "    " 
        + "option-domain-name-servers " + option_domain_name_servers + ";" + "\n" + "    " 
        + "option-domain-name" + option_domain_name + ";" + "\n  }")

    #per últim reinicim el servei dhcp i avisem al usuari de que s'ha aplicat la configuració
    os.system("sudo service isc-dhcp-server restart")
    print("\nS'ha aplicat la configuració correctament\n")



#ADRECES FIXES

def adreces_fixes():

    #Primer de tot creem variables per guardar la informació del usuari
    #per poder modificar la configuració de dhcpd
    host = input("Nom del host: ")
    mac = input("\nDirecció MAC: ")
    fixed_address = input("\nAdreça fixa: ")

    #obrim el ftixer /etc/dhcp/dhcpd.conf en mode "a" per escriure
    #al final del fitxer
    with open('/etc/dhcp/dhcpd.conf', 'a') as f:
        f.write("\n" + "host " + host + " {" + "\n" + "    " + "hardware ethernet " + mac + ";"
        + "\n" + "    " + "fixed-address " + fixed_address + ";" + "\n  }")

    #per últim reinicim el servei dhcp i avisem al usuari de que s'ha aplicat la configuració
    os.system("sudo service isc-dhcp-server restart")
    print("\nS'ha aplicat la configuració correctament\n")

#MENU
def menu_dhcp():
    
    #afegim un bluce while per a que sempre es repeteixi el menu 
    while True:
        
        #simplement esperem 4 segons per donar temps a llegir els resultats
        time.sleep(2)

        #executem la comanda clear per a fer mes agradable l'execució del menu
        os.system("clear")

        #Fem una serie de prints per a que el usuari pugui veurels 
        #i seleccionar una de les opcions
        print ("\nMENU SUPER CHULO DHCP\n")
        print ("\t1.- Instal·lar dhcp")
        print ("\t2.- Comprovar si el servei isc-dhcp-server esta instal·lat ")
        print ("\t3.- Estat del serveri DHCP ")
        print ("\t4.- Engegar/Apagar/Reinicar DHCP ")
        print ("\t5.- Mostrar llocs disponibles i actius ")
        print ("\t6.- Modificar max-lease-time ")
        print ("\t7.- Modificar default-lease-time ")
        print ("\t8.- Creació de subxarxes ")
        print ("\t9.- Creació d'adreces fixes ")
        print ("\t10.- Sortir")
    
        # sol·licitem una opcio al usuari
        opcionMenu = input("\nSelecciona una opció: ")
        
        #ara creem els valors de 1-7 per tal de que si escolleix una
        #de les 7 opcions el porti on toca
        if opcionMenu == "1":
            install_dhcp()

        elif opcionMenu == "2":
            installation_status()

        elif opcionMenu == "3":
            estat_servei_dhcp()

        elif opcionMenu == "4":
            canviar_estat_dhcp()
            
        #elif opcionMenu == "5":
        #    mostrar_llocs()
            
        elif opcionMenu == "6":
            change_max_lease_time()
            
        elif opcionMenu == "7":
            canviar_default_lease_time()
           
        elif opcionMenu == "8":
            crear_subxarxa()
            
        elif opcionMenu == "9":
            adreces_fixes()

        #en la ultima opció afegim un break per poder sortir del bucle    
        elif opcionMenu == "10":
            print("\nCHAO :)")
            break
        #Finalment fem servir else per si escolleixen una opció inexistent.
        else:
            print ("")
            input("No has sleccionat ninguna opció correcta...\nprem qualsevol tecla per continuar")
