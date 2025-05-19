from loginapp import login

def menu_cliente(cliente_obj):
    while True:
        print("\nMenú de Cliente:")
        print("1. Ver datos")
        print("2. Actualizar email")
        print("3. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print(cliente_obj.ver_datos())
        elif opcion == "2":
            nuevo_email = input("Nuevo email: ")
            print(cliente_obj.actualizar_email(nuevo_email))
        elif opcion == "3":
            print("Sesión cerrada.")
            break
        else:
            print("❌ Opción inválida.")

def main():
    while True:
        print("\n=== Menú Principal ===")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            login.registrar_usuario()
        elif opcion == "2":
            usuario = login.login_usuario()
            if usuario:
                cliente = login.clientes.get(usuario)
                if cliente:
                    menu_cliente(cliente)
        elif opcion == "3":
            print("¡Hasta la próxima!")
            break
        else:
            print("❌ Opción inválida.")

if __name__ == "__main__":
    main()