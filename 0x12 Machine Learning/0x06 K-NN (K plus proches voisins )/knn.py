# Import des bibliothèques nécessaires
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Chargement des données (vous pouvez utiliser un autre jeu de données si nécessaire)
iris = load_iris()
X = iris.data
y = iris.target

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardisation des caractéristiques
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Initialiser le classificateur K-NN
classifier = KNeighborsClassifier(n_neighbors=5)  # Spécifiez le nombre de voisins (k)

# Entraîner le modèle K-NN
classifier.fit(X_train, y_train)

# Prédire les étiquettes pour l'ensemble de test
y_pred = classifier.predict(X_test)

# Calculer la précision du modèle
accuracy = accuracy_score(y_test, y_pred)
print("Précision du modèle K-NN : {:.2f}%".format(accuracy * 100))

#knn-yt bla graph
# Import des bibliothèques nécessaires
import numpy as np   # pour les calculs numériques
import pandas as pd  # pour la manipulation des données
import matplotlib.pyplot as plt  # pour les visualisations
from sklearn.model_selection import train_test_split # pour diviser les données en ensembles d'entraînement et de test
from sklearn.neighbors import KNeighborsClassifier # pour le modèle KNN
from sklearn.datasets import load_digits # pour charger les données de digits
from sklearn.metrics import confusion_matrix # pour la matrice de confusion

# Chargement des données
digits = load_digits() # chargement des données
X = digits.data # les données   
y = digits.target # les étiquettes  

# Division des données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)  # 80% train, 20% test

# Création du modèle KNN
knn = KNeighborsClassifier(n_neighbors=5) # initialisation du modèle avec k=5
knn.fit(X_train, y_train) # apprentissage du modèle

# Calcul du taux de précision
score = knn.score(X_test, y_test) # évaluation du modèle
print('Taux de précision :', score) # affichage du taux de précision

# Tester k de 1 à 20
neighbors = np.arange(1, 21)  # k de 1 à 20
train_accuracy = np.empty(len(neighbors))   # initialisation de la précision sur l'ensemble d'entraînement
test_accuracy = np.empty(len(neighbors))   # initialisation de la précision sur l'ensemble de test

for i, k in enumerate(neighbors):  # boucle sur les valeurs de k
    
    knn = KNeighborsClassifier(n_neighbors=k) # initialisation du modèle avec la valeur de k courante
    knn.fit(X_train, y_train) # apprentissage du modèle
    train_accuracy[i] = knn.score(X_train, y_train) # précision sur l'ensemble d'entraînement
    test_accuracy[i] = knn.score(X_test, y_test) # précision sur l'ensemble de test

print(test_accuracy) # affichage de la précision sur l'ensemble de test

# Prédiction sur l'ensemble de test
y_pred = knn.predict(X_test)

# Matrice de confusion
cm = confusion_matrix(y_test, y_pred) # matrice de confusion
print(cm) # affichage de la matrice de confusion

# Nombre d'occurrences de chaque classe dans y_test
print(np.bincount(y_test))

#knn-darija
from sklearn.datasets import load_iris #bach nkhedmo b database d library
from sklearn.model_selection import train_test_split #bach nqesmo data li 3endna
from sklearn.neighbors import KNeighborsClassifier #bach nkhedmo b model knn
from sklearn.metrics import accuracy_score #bach nkhedmo b accuracy w ndiro matrix confusion
#1 haja khas njibo data
iris = load_iris()
#2 haja ne3tiw m X data w y target
X, y = iris.data, iris.target
#3 khas nqesmo data dyalna
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 
#4 nsaybo lmodel s 3tina l k = 3
k = 3
knn = KNeighborsClassifier(n_neighbors=k)
#5 entriniw l module 
knn.fit(X_train, y_train)
#6 nkhedmo b predict
y_pred = knn.predict(X_test)
#7 nkhedmo b accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")