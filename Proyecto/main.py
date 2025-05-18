from clienteapp import Cliente

def main():
    print("Registro de clientes")
    
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    email = input("Ingrese su email: ")

    cliente = Cliente(nombre, edad, email)
    print(cliente)

    print ("\nCliente registrado correctamente: ")
    print(cliente.ver_datos())

    print("\n Desea acualizar su email? (s/n)")
    respuesta = input().lower()

    if respuesta == "s":
        nuevo_email = input("Ingrese su nuevo email: ")
        print(cliente.actualizar_email(nuevo_email))
    else:
        print("No se actualizó su email.")

    print("\nSus datos ingresados son: ")
    print(cliente.ver_datos())
    print("\nGracias por registrarse!")

if __name__ == "__main__":
    main()