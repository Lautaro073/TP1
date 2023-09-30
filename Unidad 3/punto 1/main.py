import numpy as np
import matplotlib.pyplot as plt

# Tamaño de las casas en metros cuadrados
X = np.array([10, 20, 40, 60, 80, 100, 150])

# Precio de las casas en pesos argentinos (ARS)
Y = np.array([500000, 550000, 650000, 800000, 950000, 1200000, 1550000])

def simple_linear_regression(X, Y):
    n = len(X)
    
    # Calcula las medias de X e Y
    mean_x = np.mean(X)
    mean_y = np.mean(Y)
    
    # Calcula los coeficientes de la regresión
    SS_xy = np.sum(Y*X) - n*mean_y*mean_x
    SS_xx = np.sum(X*X) - n*mean_x*mean_x
    
    b1 = SS_xy / SS_xx
    b0 = mean_y - b1*mean_x
    
    return b0, b1

b0, b1 = simple_linear_regression(X, Y)

# Predice el precio de una casa de 90 metros cuadrados
size = 90
predicted_price = b0 + b1 * size
print(f"El precio predicho para una casa de {size} metros cuadrados es: ${predicted_price:.2f} ARS")

# Visualiza los datos y la línea de regresión
plt.scatter(X, Y, color='blue', label='Datos reales')
plt.plot(X, b0 + b1 * X, color='red', label='Línea de regresión')
plt.xlabel('Tamaño de la casa (m^2)')
plt.ylabel('Precio (ARS)')
plt.legend()
plt.show()
