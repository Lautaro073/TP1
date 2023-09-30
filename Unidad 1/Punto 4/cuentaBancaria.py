class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0.0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Depósito exitoso. Nuevo saldo: ${self.saldo:.2f}")
        else:
            print("El monto del depósito debe ser mayor que cero.")

    def retirar(self, monto):
        if monto > 0 and monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro exitoso. Nuevo saldo: ${self.saldo:.2f}")
        elif monto <= 0:
            print("El monto del retiro debe ser mayor que cero.")
        else:
            print("Fondos insuficientes para realizar el retiro.")

    def consultar_saldo(self):
        print(f"Saldo actual de la cuenta de {self.titular}: ${self.saldo:.2f}")


# Función principal para interactuar con el usuario
def main():
    titular = input("Ingrese el nombre del titular de la cuenta: ")
    saldo_inicial = float(input("Ingrese el saldo inicial de la cuenta: "))
    cuenta = CuentaBancaria(titular, saldo_inicial)

    while True:
        print("\nOpciones:")
        print("1. Consultar saldo")
        print("2. Realizar depósito")
        print("3. Realizar retiro")
        print("4. Salir")

        opcion = input("Seleccione una opción (1/2/3/4): ")

        if opcion == "1":
            cuenta.consultar_saldo()
        elif opcion == "2":
            monto = float(input("Ingrese el monto a depositar: "))
            cuenta.depositar(monto)
        elif opcion == "3":
            monto = float(input("Ingrese el monto a retirar: "))
            cuenta.retirar(monto)
        elif opcion == "4":
            print("Gracias por utilizar nuestro servicio.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()
