class Cliente:
    tipo = "Cliente logeado"
    contador = 0  

    def __init__(self, nombre: str, edad: int, email: str):
        Cliente.contador += 1
        self.id_cliente = Cliente.contador
        self.nombre = nombre
        self.edad = edad
        self.email = email

    def __str__(self):
        return f"Cliente {self.nombre} (ID: {self.id_cliente})"

    def ver_datos(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Email: {self.email}"

    def actualizar_email(self, nuevo_email: str):
        self.email = nuevo_email
        return f"Email actualizado a: {self.email}"