
# Correction Control 2

1. Définitions :
   - **Apprentissage automatique (Machine Learning, ML)** : L'apprentissage automatique est une branche de l'intelligence artificielle qui permet à un système d'apprendre à partir des données et d'améliorer ses performances sans être explicitement programmé. Il utilise des algorithmes statistiques pour donner aux ordinateurs la capacité d'« apprendre » avec des données et de faire des prédictions ou des décisions basées sur ces données.
   - **Données dans l’ML** : Les données dans le Machine Learning désignent l'ensemble des informations (ensemble de données ou dataset) utilisées pour entraîner, tester et valider les modèles d'apprentissage automatique. Ces données peuvent être structurées (comme des tableaux ou des bases de données) ou non structurées (comme du texte ou des images), et sont essentielles pour développer des modèles précis et efficaces.

2. Types d'apprentissage automatique et exemples d'algorithmes :
   - **Apprentissage supervisé** : Les algorithmes sont entraînés sur des données étiquetées. Exemples : Régression linéaire, SVM.
   - **Apprentissage non supervisé** : Les algorithmes analysent et regroupent des ensembles de données non étiquetées. Exemples : K-means, Analyse en composantes principales (PCA).

3. **Différence entre régression et classification**
   - La **régression** est utilisée pour prédire une valeur continue, telle que le prix d'une maison, le salaire d'une personne, ou la température. Le but est de trouver la relation fonctionnelle entre les variables indépendantes (prédictives) et une variable dépendante continue.
   - La **classification** est utilisée pour prédire une étiquette de catégorie, comme déterminer si un email est spam ou non, ou classifier une image parmi plusieurs catégories. La sortie est une variable catégorique.

**Exercice N°2:**

1. **Charger la base de données IRIS du fichier «IRIS.csv»**  
   ```python
   import pandas as pd
   iris = pd.read_csv('IRIS.csv')
   ```

2. **Afficher l'en-tête de la base de données**  
   ```python
   print(iris.head())
   ```

3. **Sélectionner les colonnes et diviser les données**  
   - Sélection des données et des étiquettes :
     ```python
     X = iris.iloc[:, :-1]  # toutes les colonnes sauf la dernière
     y = iris.iloc[:, -1]  # dernière colonne
     ```
   - Séparation en données d'apprentissage et de test :
     ```python
     from sklearn.model_selection import train_test_split
     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)
     ```

4. **Importer et instancier le modèle SVC avec un noyau linéaire, puis entraîner le modèle**  
   ```python
   from sklearn.svm import SVC
   model = SVC(kernel='linear')
   model.fit(X_train, y_train)
   ```

Ces extraits de code Python supposent que vous avez accès à un environnement Python avec les bibliothèques nécessaires installées. Utilisez ces commandes pour réaliser les tâches demandées dans l'exercice.

Voici comment répondre aux questions 5, 6 et 7 de votre exercice :

5. **Calculer le vecteur des prédictions sur les données du test**
   ```python
   y_pred = model.predict(X_test)
   ```

6. **Calculer la justesse (accuracy) en utilisant la fonction score()**
   ```python
   accuracy = model.score(X_test, y_test)
   print(f"L'accuracy du modèle est de {accuracy:.2f}")
   ```

7. **Calculer la matrice de confusion en utilisant sklearn.metrics**
   ```python
   from sklearn.metrics import confusion_matrix
   cm = confusion_matrix(y_test, y_pred)
   print("Matrice de confusion :")
   print(cm)
   ```

**@xDweb**