import os
import sys
import subprocess
import time

#ver el estado de instalación de apache.
def estado_instalacion():
    os.system("dpkg --get-selections | grep apache")

#instalar apache2

def install_apache():
    os.system("sudo apt install apache2")

#ver el estado del servicio apache.
def estado_apache():
    os.system("sudo service apache2 status")
    os._exit(1)

#parte de programa para listar los sitios disponibles
def listar_sites():
    print("Estos son los sitos disponibles: \n")
    listarr = os.listdir("/etc/apache2/sites-available")#utilizar la siguiente ruta para mostara los sitios disponibles.
    print (listarr)

#ver lo sitios habilitados
def listar_habilitados():
    print("Estos son los sitios habilitados: \n")
    listarhabi = os.listdir("/etc/apache2/sites-enabled")
    print (listarhabi)

#encender/apagar/reinicar-apache
def canviar_estado_apache():

    estat = input("\nEncender / Apagar / Reiniciar :")
    
    if estat == "Encender":
        
        print("Encendiendo el servicio apache...\n")
    
        os.system("sudo service apache2 start")
        
        time.sleep(2)

        print("Servecio apache encendido\n")
                
    elif estat == "Apagar":
                        
        print("Apagando el servicio...\n")

        os.system("sudo service apache2 stop")
    
        time.sleep(2)

        print("Servicio apache apagado\n")

    elif estat == "Reiniciar":
        
        print("Reiniciando el servicio..\n")

        os.system("sudo service apache2 restart")
    
        time.sleep(2)

        print("Servicio apache reiniciado\n")
    
    else:
        print ("")
        input("No has sleccionat ninguna opció correcta...\nprem qualsevol tecla per continuar")



#parte de programa para habilitar y deshabilitar sitios.
def hd():
    entero = input("Quires habilitar o deshabilitar sitio?[h/d]: ")
    #condicion si el usaurio pone h es para habiliar y si pone d para deshabilitar, y que dependiando lo que haya escogido le ejecutara los siguentes comando.
    if (entero == "h"):
        entero2 = input("Pon el nombre del sitio que quieres hanilitar: ")
        subprocess.call(["a2ensite", entero2])#utilizar el comando a2ensite para habilitar los sitios.
        restart = subprocess.run(['systemctl reload apache2'], shell=True)
        print(restart)
    elif (entero == "d"):
        entero3 = input("Pon el nombre del sitio que quieres hanilitar: ")
        subprocess.call(["a2dissite", entero3])#utilizar el comando a2dissite para deshabilitar sitios.
        restart = subprocess.run(['systemctl reload apache2'], shell=True)
        print(restart)
    else:
        print ("Error")    

def crear_sites():
    #global vhost
    #input
    #vhost = entero2()
    vhost = input("Pon un nombre de dominio para tu sitio virtual: ")
    cmd = "mkdir /var/www/{0}".format(vhost)#cuando el usuario pone el nombre del sitios se le va a crear una carpeta en la ruta de /var/www
    os.system(cmd)
    
    #añadir permisos
    cmd = "chown -R $USER:$USER /var/www/{0}".format(vhost)
    os.system(cmd)
    
    cmd = "chmod -R 755 /var/www/{0}".format(vhost)
    os.system(cmd)
    
    
    #crear un fichero html cuando el usuario haya creado el sitio.
    filename = '/var/www/{0}/index.html'.format(vhost)
    f = open(filename, 'w')
    f.write("<html><head><title>Hola que hace</title></head><body><h1>Holaaaaaaa</h1></body></html>")
    f.close()
    
    #lo que contendra el fichero de conf del sitio que haya creado el usuario.
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
    
    #habilitar el sitio que haya creado el usuario
    cmd = "a2ensite {0}".format(vhost)
    os.system(cmd)
    
    #deshabilitar el sitio por defecto
    cmd = "a2dissite 000-default.conf"
    os.system(cmd)
    
    #mostrara el comando de conf
    cmd = "apache2ctl configtest"
    os.system(cmd)
    
    #reiniciar apache2
    cmd = "systemctl restart apache2"
    os.system(cmd)

#menu
def menu_apache():
    print("=====================Ejecuta una opción=======================")
    print("=1. Ver el estado de instalación.                            =")
    print("=2. Instalar apache.                                         =")
    print("=3. Ver el estado del servicio.                              =")
    print("=4. Encender / Apagar / Reinicar.                            =")
    print("=5. Listar sitios disponibles.                               =")
    print("=6. Habilitar/Deshabilitar sitios.                           =")
    print("=7. Crear sitios.                                            =")
    print("=8. Listar sitios habilitados.                               =")
    print("=9. Exit.                                           		=")
    print("=====================Fin del programa=========================")

    #parte de la función menu.
    while True:
        
        option = input("Ingresa una opción: ")
        
        if option == "1":
            estado_instalacion()

        elif option == "2":
            install_apache()

        elif option == "3":
            estado_apache()

        elif option == "4":
            canviar_estado_apache()

        elif option == "5":
            listar_sites()

        elif option == "6":
            hd()
        
        elif option == "7":
            crear_sites()

        elif option == "8":
            listar_habilitados()

        elif option == "9":
            print("\nCHAO :)")
            break
        
        else:
            print ("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")

         
        