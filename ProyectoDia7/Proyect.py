#Cuenta bancaria de un cliente
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def imprimir(self):
        print(f"Cliente: {self.nombre} {self.apellido} | Cuenta: {self.numero_cuenta} | Balance: {self.balance}")

    def depositar(self, cantidad):
        self.balance += cantidad

    def retirar(self, cantidad):
        if cantidad > self.balance:
            print("Fondos insuficientes.")
        else:
            self.balance -= cantidad


def crear_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    numero_cuenta = input("Ingrese el número de cuenta: ")
    balance = float(input("Ingrese el balance inicial: "))
    return Cliente(nombre, apellido, numero_cuenta, balance)


def inicio():
    cliente = crear_cliente()
    while True:
        eleccion = int(input("1. Depositar  2. Retirar  3. Salir: "))
        match eleccion:
            case 1:
                cantidad = float(input("Ingrese la cantidad: "))
                cliente.depositar(cantidad)
                cliente.imprimir()
            case 2:
                cantidad = float(input("Ingrese la cantidad: "))
                cliente.retirar(cantidad)
                cliente.imprimir()
            case 3:
                print("Que le vaya bien, gracias.")
                break


inicio()