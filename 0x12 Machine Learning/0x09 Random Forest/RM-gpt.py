import numpy as np   # pour les calculs numériques
import pandas as pd  # pour la manipulation des données
from sklearn.datasets import load_iris # pour charger l'ensemble de données Iris
from sklearn.cluster import KMeans # pour l'algorithme K-Means
from sklearn.metrics import confusion_matrix # pour la matrice de confusion

# Chargement de l'ensemble de données Iris
iris = load_iris()
X = iris.data # les données   

# Création du modèle K-Means
kmeans = KMeans(n_clusters=3) # spécifie le nombre de clusters à rechercher
kmeans.fit(X) # apprentissage du modèle

# Prédiction des clusters pour chaque point de données
y_kmeans = kmeans.predict(X)

# Affichage des clusters assignés à chaque échantillon
print("Clusters assignés à chaque échantillon :\n", y_kmeans)

# Affichage des coordonnées des centres de clusters
print("\nCoordonnées des centres de clusters :\n", kmeans.cluster_centers_)

# Calcul de la matrice de confusion
conf_matrix = confusion_matrix(iris.target, y_kmeans)
print("\nMatrice de confusion :\n", conf_matrix)

