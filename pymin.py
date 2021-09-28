"""
MENU PYMIN

Nafsu / Sergi / Alex / Dani
"""

#Importem els moduls necessaris
import os
import time
from adminlinux import menu_admin_linux
from apache import menu_apache
from menu_ssh import menu_ssh
from menu_pla_dhcp import menu_dhcp

#Definim un menu principal que serà la base per accedir als altres menus.
#De tal manera que nomes es mostri un menu a la vegada fent mes agradable
#la seva execució i visió.
def pymin_menu():
    
    #afegim un bluce while perque es repeteixi constanment
    while True:
    
        #simplement esperem 2 segons per donar temps a llegir els resultats
        time.sleep(2)
        
        #Fem una serie de prints per a que el usuari pugui veurels 
        #i seleccionar una de les opcions
        print ("\nMENU ADMIN_LINUX_PYTHON\n")
        print ("\t1.- Administració d'usuaris a linux")
        print ("\t2.- Web - Apache ")
        print ("\t3.- SSH ")
        print ("\t4.- DHCP ")
        print ("\t5.- Sortir")
           
        # sol·licitem una opció al usuari
        opcionMenu = input("\nSelecciona una opció: ")
        
        #ara creem els valors de per tal de que si escolleix una
        #de les opcions executi el menu adient.
        if opcionMenu == "1":
            menu_admin_linux()
            
        elif opcionMenu == "2":
            menu_apache()
            
        elif opcionMenu == "3":
            menu_ssh()
            
        elif opcionMenu == "4":
            menu_dhcp()
           
        #en la ultima opció afegim un break per poder sortir del bucle
        #i ens porti de nou al menu principal   
        elif opcionMenu == "5":
            print("\nCHAO :)")
            break
        
        #Finalment fem servir else per si escolleixen una opció inexistent.
        else:
            print ("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
        
pymin_menu()