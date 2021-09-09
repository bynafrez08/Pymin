"""
MENU DHCP

"""

#importem los módulos necesarios
import os
import time

#VEURE SI DHCP ESTA INSTALADO
#Utlitzem la siguiente comando para comprobar si dhcp esta instalado
def veure_dhcp():
    os.system("apt list | grep isc-dhcp-server")

#ESTAT DEL SERVICIO

def estat_servei_dhcp():
        
    os.system("sudo service isc-dhcp-server status")

    time.sleep(5)

#shutdown, restart, status, start

def canviar_estat_dhcp():

    estat = input("\nStart / Shutdwon / Restart :")
    
    if estat == "Start":
        
        print("Poniendo en marcha el servicio...\n")
    
        os.system("sudo service isc-dhcp-server start")
        
        time.sleep(2)

        print("Servicio dhcp marcha\n")
                
    elif estat == "Shutdown":
                        
        print("Parando el servidor...\n")

        os.system("sudo service isc-dhcp-server stop")
    
        time.sleep(2)

        print("Servidor DHCP parado\n")

    elif estat == "Restart":
        
        print("Reiniciando el servicio..\n")

        os.system("sudo service isc-dhcp-server restart")
    
        time.sleep(2)

        print("Servicio dhcp marcha\n")
    
    else:
        print ("")
        input("No seleccionado ninguna opción correcta ...\n pulsa cualquier tecla para continuar")

#INSTALAR DHCP

#utlitzem os.system para ejecutar un pedido en el terminal de linux.
def install_dhcp():
    os.system("sudo apt -y install isc-dhcp-server ")

#MOSTRAR SITIOS ACTIVOS Y DISPONIBLES
def mostrar_llocs():

    #open dhcpd.conf 
    file = open("/etc/dhcp/dhcpd.conf", "r")

    print("\nSi no tienes ninguna subred ni host create no se mostrará nada\n")
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

    file.close()

#MAX_LEASE_TIME

def canviar_max_lease_time():

    #obrim el dhcp.conf y leemos el fichero para guardar su
     #contingut en la variable fecha
    with open('/etc/dhcp/dhcpd.conf', 'r') as f:
        data = f.readlines()

    #Utlitzem print para mostrar en pantalla cuál es el max_lease actual
     #Aixo lo hacemos al especificar el numero de linea dentro del dhcp.conf que queremos mostrar
     #EN este caso la fila 13 cuento por defecto el max-lease, y utilizaremos el mismo con los otros archivos
    print("\nmax-lease-time actual: \n")
    print(data[13])

    #crear una variable per a que el usuario escriba el nuevo variable de max-lease
    nou_max = input("Modifica el max-lease-time (Has d'escriure el següent): \nmax-lease-time 600; (o el numero que vulguis): ")
    
    #Como en el caso anterior abrimos el archivo pero en este caso modo escritura
    #escribimos la variable introducida por un usuario a la linea 13
    data[13] = nou_max + "\n"
    with open('/etc/dhcp/dhcpd.conf', 'w') as f:
        f.writelines(data)
        f.close()

    with open('/etc/dhcp/dhcpd.conf', 'r') as f:
        data = f.readlines()

    #pera terminar volvemos a mostrar por pantalla el max-lease actual.
    print("\nmax-lease-time actual: \n")
    print(data[13])
    f.close()



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
        time.sleep(5)

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
            veure_dhcp

        elif opcionMenu == "3":
            estat_servei_dhcp()

        elif opcionMenu == "4":
            canviar_estat_dhcp()
            
        elif opcionMenu == "5":
            mostrar_llocs()
            
        elif opcionMenu == "6":
            canviar_max_lease_time()
            
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
