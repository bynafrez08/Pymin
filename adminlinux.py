import os
import sys
import crypt
import subprocess
import getpass

#parte de programa para listar los usarios debajo de /home
def mostrar():
    print("Estos son los usuarios debajo de /home: \n")
    listar = os.listdir("/home")#utilizar la funcion os.listdir para mostrar conetent de un directorio.
    print (listar)

#parte de programa para crear usuario en linux.
def crearusuario():
    uname = input("Nombre de usuario: ")
    upass = input("Contraseña: ")
    # preguntar por el  usuario
    ucrypt =  crypt.crypt(upass, "123")
    crearl = os.system("useradd -m -p "+upass+" "+uname)#utiliza el comando userdel -m -p para crear el /home y grupo del usuario.
    print("Usuario creado correctamente")

#parte de programa para eliminar usuario.
def delete_user():
    username = input("Nombre de usuario : ")
  
    try:
        output = subprocess.run(['userdel', username ])#utilizar userdel para eliminar usuario.
        if output.returncode == 0:
            print("Se ha eliminado correctamente")
    except:
        print(f"Error no se puede eliminar el usuario.")
        sys.exit(1)
    #tambien especifico que elimine el dir /home del usuario a la hora de eliminar el usuario.
    home_dir = "/home/" + username
    if os.path.exists(home_dir):
        subprocess.call(['rm','-r',home_dir])

#menu
def menu_admin_linux():
    print("=====================Ejecuta una opción=======================")
    print("=1. Mostrar usuario de bajo /home.                           =")
    print("=2. Crear usuarios.                                          =")
    print("=3. Eliminar usuario.                                        =")
    print("=4. Exit.                                                    =")
    print("=====================Fin del programa=========================")

    #parte de la funcion menu.
    while True:
    
        option = (input("\nIngresa una opción: "))
        
        if option == "1":
            mostrar()

        elif option == "2":
            crearusuario()

        elif option == "3":
            delete_user()
  
        elif option == "4":
            print("\nCHAO :)")
            break

        else:
            print ("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")

