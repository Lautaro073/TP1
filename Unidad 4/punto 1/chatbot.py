import requests

API_KEY = '6fb33cb6f14141169b4192145232809'  # clave API  de WeatherAPI
BASE_URL = 'http://api.weatherapi.com/v1/current.json?'

def obtener_clima(ciudad):
    url = f"{BASE_URL}key={API_KEY}&q={ciudad}&lang=es"  # Solicitamos datos en español
    
    response = requests.get(url)
    data = response.json()

    if 'error' in data:
        return data['error']['message']

    location = data['location']
    current = data['current']
    
    nombre_ciudad = location['name']
    pais = location['country']
    temperatura = current['temp_c']
    condicion = current['condition']['text']
    humedad = current['humidity']
    presion = current['pressure_mb']

    respuesta = (f"En {nombre_ciudad}, {pais}:\n"
                 f"Temperatura: {temperatura}°C\n"
                 f"Condiciones: {condicion}\n"
                 f"Humedad: {humedad}%\n"
                 f"Presión: {presion} hPa")

    return respuesta

def main():
    print("¡Hola! Soy tu chatbot del clima. ¿Para qué ciudad deseas conocer el clima actual?")
    
    while True:
        ciudad = input("Introduce el nombre de la ciudad (o 'salir' para terminar): ")
        
        if ciudad.lower() == 'salir':
            print("¡Hasta pronto!")
            break
        
        print(obtener_clima(ciudad))

if __name__ == '__main__':
    main()
