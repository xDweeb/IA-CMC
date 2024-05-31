#k-means-yt
#n3eyto l library li ghadi nkhedmo bihum
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import datasets

#n3eyto l data li ghadi nkhedmo biha
iris = datasets.load_iris()

#naffichiw data
print(iris.data)

#n stockiwha f dataframe pandas
x = pd.DataFrame(iris.data)

#n difinw les noms dyal les colonnes
x.columns = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width']
y = pd.DataFrame(iris.target) 
y.columns = ['classe']

#repartition d datasets f scatter plot 2d
plt.scatter(x.Petal_Length, x.Petal_Width)

#visualisation les classes de notre dataset
colorL = np.array(['red', 'green', 'blue'])
plt.scatter(x.Petal_Length, x.Petal_Width, c=colorL[iris.target], s=20)

#utilise la methode elbow pour determiner le nombre optimal de cluster
inert = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i)
    kmeans.fit(x)
    inert.append(kmeans.inertia_)
    
#affichage la courbe de la methode elbow
plt.plot(range(1, 11), inert)
plt.title('Methode Elbow')
plt.xlabel('Nombre de clusters')
plt.ylabel('Inertie')
plt.show()

#cluster k-means
model = KMeans(n_clusters=3) 
model.fit(x)

model.labels_

 #visualiser les classes predites par k-means
colorL = np.array(['red', 'green', 'blue'])
plt.scatter(x.Petal_Length, x.Petal_Width, c=colorL[model.labels_], s=20)

#visualise les classe origins et predites par le model
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3))
fig.suptitle('K-means')
ax1.scatter(x.Petal_Length, x.Petal_Width, c=colorL[iris.target], s=20)
ax2.scatter(x.Petal_Length, x.Petal_Width, c=colorL[model.labels_], s=20)


#matrice de confusion
from sklearn.metrics import confusion_matrix
matrice = confusion_matrix(iris.target, model.labels_)
matrice

#sans graphique
# Importation des bibliothèques nécessaires
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn import datasets

# Chargement des données
iris = datasets.load_iris()

# Stockage des données dans un DataFrame pandas
x = pd.DataFrame(iris.data)
x.columns = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width']

# Utilisation de la méthode elbow pour déterminer le nombre optimal de clusters
inert = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(x)
    inert.append(kmeans.inertia_)

# Cluster K-Means
model = KMeans(n_clusters=3) 
model.fit(x)

# Matrice de confusion
from sklearn.metrics import confusion_matrix
matrice = confusion_matrix(iris.target, model.labels_)
print(matrice)

#code-gpt
# Importation des bibliothèques nécessaires
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
