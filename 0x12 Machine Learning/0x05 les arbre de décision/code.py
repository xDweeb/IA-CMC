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
#le paramètre min_samples_lear donne le nomber minimal