# Nombre del archivo de texto
nombre_archivo = "contPalabras.txt"

# Inicializamos el contador de palabras
contador_palabras = 0

try:
    # Abrir el archivo en modo lectura
    with open(nombre_archivo, 'r') as archivo:
        # Leer el contenido del archivo línea por línea
        for linea in archivo:
            # Dividir la línea en palabras usando espacio como separador
            palabras = linea.split()
            # Incrementar el contador de palabras con la cantidad de palabras en la línea
            contador_palabras += len(palabras)

    # Mostrar el resultado
    print(f"El archivo '{nombre_archivo}' contiene {contador_palabras} palabras.")

except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no fue encontrado.")

except Exception as e:
    print(f"Ocurrió un error: {str(e)}")
