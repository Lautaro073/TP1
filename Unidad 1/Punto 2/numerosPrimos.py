def es_primo(numero):
    if numero <= 1:
        return False  # Los números menores o iguales a 1 no son primos

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False  # Si es divisible por algún número en este rango, no es primo

    return True  # Si no es divisible por ningún número en el rango, es primo


# Ejemplo de uso:
numero = int(input("Ingresa un número: "))
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")
