import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Generar datos aleatorios
data, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Visualizar los datos generados
plt.scatter(data[:, 0], data[:, 1], s=50)
plt.show()

# Implementar K-means
kmeans = KMeans(n_clusters=4)
kmeans.fit(data)
predicted_labels = kmeans.predict(data)

# Visualizar los clusters formados
plt.scatter(data[:, 0], data[:, 1], c=predicted_labels, s=50, cmap='viridis')

# Mostrar los centroides de los clusters
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.75, marker='X')
plt.show()
