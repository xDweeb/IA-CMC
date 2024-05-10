#import les libraries
import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris

#charger le dataset Iris
iris = load_iris()
X, y = iris.data, iris.target

#Combien y a-t-il d'exemples de chaque classe?
np.bincount(iris.target)

#Creation jeu d'apprentissage et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#Construire un arbre de décision
modelTree = tree.DecisionTreeClassifier()
modelTree.fit(X_train, y_train)

#Calculer le taux de performance du modèle
accuracyTreeTest = modelTree.score(X_test, y_test)
print('Accuracy Arbre x_test :', accuracyTreeTest)

# Tester les paramètres max_depth et min_samples_split
#le paramètre max_depth est un seuil sur la profondeur de l'arbre
#le paramètre min_samples_lear donne le nomber minimal d'echantillons dans un noeud feuille.
#Ile permettent de mettre des containers sur la construction de l'arbre
#et donc de controler indirectement le phénomène de sur-apprentissage
for mdepth in [1, 2, 3, 4, 10]:
    clf = tree.DecisionTreeClassifier(max_depth=mdepth)
    clf = clf.fit(X_train, y_train)
    print(clf.score(X_test, y_test))

for msplit in [2, 3, 5, 10, 20]:
    clf = tree.DecisionTreeClassifier(min_samples_split=msplit)
    clf = clf.fit(X_train, y_train)
    print(clf.score(X_test, y_test))

#Prédiction test
modelTree.predict([[1.0,1.0,5.4,0.89]])

