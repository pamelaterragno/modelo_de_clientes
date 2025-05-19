from clienteapp.cliente import Cliente

# Diccionarios globales para almacenamiento en memoria
usuarios = {}   # nombre_usuario → contraseña
clientes = {}   # nombre_usuario → objeto Cliente

def registrar_usuario():
    """
    Permite registrar un nuevo usuario, con reintentos si ya existe o hay datos inválidos.
    """
    print("\nRegistro de nuevo usuario")
    intentos = 0
    max_intentos = 2

    while intentos < max_intentos:
        nombre_usuario = input("Nombre de usuario: ")

        if nombre_usuario in usuarios:
            print("❌ Ese usuario ya existe. Intente con otro.")
            intentos += 1
            continue

        password = input("Contraseña: ")
        nombre = input("Nombre completo: ")

        try:
            edad = int(input("Edad: "))
        except ValueError:
            print("❌ Edad inválida.")
            intentos += 1
            continue

        email = input("Email: ")
        if "@" not in email:
            print("❌ Email inválido. Debe contener '@'.")
            intentos += 1
            continue

        # Si todo está OK, registramos
        usuarios[nombre_usuario] = password
        clientes[nombre_usuario] = Cliente(nombre, edad, email)
        print("✅ Usuario y cliente registrados correctamente.")
        return

    print("⛔ Se alcanzó el número máximo de intentos.")

def login_usuario():
    """
    Permite iniciar sesión. Valida usuario y contraseña con hasta 2 intentos cada uno.
    """
    print("\nInicio de sesión")
    max_intentos = 2
    intentos_usuario = 0

    while intentos_usuario < max_intentos:
        nombre_usuario = input("Usuario: ")

        if nombre_usuario in usuarios:
            intentos_clave = 0
            while intentos_clave < max_intentos:
                password = input("Contraseña: ")
                if usuarios[nombre_usuario] == password:
                    print(f"Bienvenido/a, {nombre_usuario}!")
                    return nombre_usuario
                else:
                    print("❌ Contraseña incorrecta.")
                    intentos_clave += 1

            print("⛔ Máximo de intentos de contraseña alcanzado.")
            return None
        else:
            print("❌ Usuario no encontrado.")
            intentos_usuario += 1

    print("⛔ Máximo de intentos para el usuario alcanzado.")
    return None
