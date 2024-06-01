
# Correction Control 3

1. **Différence entre l'apprentissage automatique et l'apprentissage profond**
   - **L'apprentissage automatique** (Machine Learning) est une branche de l'intelligence artificielle qui englobe les techniques permettant aux ordinateurs d'apprendre à partir des données et d'améliorer leurs performances sans programmation explicite. Cela inclut des méthodes variées comme la régression linéaire, les arbres de décision, et les SVM.
   - **L'apprentissage profond** (Deep Learning) est un sous-ensemble de l'apprentissage automatique qui utilise des réseaux de neurones profonds (deep neural networks) avec de nombreuses couches cachées. Ces modèles sont particulièrement puissants pour traiter des volumes élevés de données non structurées, comme les images et le son, où ils peuvent automatiquement détecter des caractéristiques pertinentes sans intervention humaine.

2. **Deux sources d'erreurs en apprentissage qui peuvent affecter les performances d'un modèle**
   - **Biais de données** : Si les données d'entraînement ne sont pas représentatives de la population générale, le modèle peut développer un biais et ne pas bien généraliser sur de nouvelles données.
   - **Variance élevée** : Si un modèle est trop complexe, il peut apprendre des détails et du bruit des données d'entraînement à un tel point qu'il échoue à bien généraliser sur de nouvelles données, un phénomène souvent appelé sur-apprentissage.

3. **Différence entre sous-apprentissage et sur-apprentissage**
   - **Sous-apprentissage** : Se produit lorsque le modèle est trop simple pour capturer la structure sous-jacente des données. Il ne performe pas bien même sur les données d'entraînement, ce qui indique qu'il n'a pas appris les tendances pertinentes dans les données.
   - **Sur-apprentissage** : Se produit lorsque le modèle est trop complexe et apprend trop bien les détails et le bruit dans les données d'entraînement, au point de perdre sa capacité à généraliser à partir de nouvelles données. Le modèle performe très bien sur les données d'entraînement mais mal sur les données de test ou de validation.

4. **Comment détecter le surapprentissage ?**
   - Une manière de détecter le surapprentissage est de comparer les performances du modèle sur les données d'entraînement par rapport à celles sur les données de test ou de validation. Si le modèle performe significativement mieux sur les données d'entraînement que sur les données de test, cela peut indiquer un surapprentissage.
   - Une autre méthode consiste à utiliser une visualisation comme une courbe d'apprentissage, où l'on observe l'évolution de l'erreur d'entraînement et de l'erreur de validation en fonction du nombre d'itérations d'apprentissage. Un écart croissant entre ces deux erreurs peut également signaler un surapprentissage.

5. **Trois techniques de régularisation :**
   - **La régularisation L1 (Lasso)** : Pénalise la somme des valeurs absolues des coefficients de régression, conduisant à la réduction (ou l'annulation) de certains coefficients, ce qui simplifie le modèle.
   - **La régularisation L2 (Ridge)** : Pénalise la somme des carrés des coefficients de régression, ce qui aide à réduire leur impact sans les éliminer complètement, menant à un modèle moins sensible au bruit des données.
   - **Dropout** : Utilisée principalement dans les réseaux de neurones, cette technique consiste à "ignorer" aléatoirement certaines unités (neurones) durant la phase d'entraînement, ce qui aide à éviter la dépendance excessive du modèle à des caractéristiques spécifiques des données d'entraînement.

6. **Définition de l'architecture d'un réseau de neurones convolutif :**
   - Un **réseau de neurones convolutif (CNN)** est un type de réseau de neurones profond souvent utilisé pour analyser des images. Il est composé de plusieurs types de couches, dont les principales sont :
     - **Couches convolutives** : Elles appliquent une convolution qui traite les données d'entrée avec des filtres pour créer des cartes de caractéristiques, capturant des aspects essentiels comme les bords ou les textures.
     - **Couches de pooling (subsampling)** : Elles réduisent les dimensions spatiales des cartes de caractéristiques pour diminuer la complexité computationnelle et le surapprentissage.
     - **Couches de normalisation** : Elles normalisent les entrées pour chaque neurone, ce qui aide à accélérer la convergence du réseau.
     - **Couches entièrement connectées** : Elles prennent les caractéristiques extraites et apprennent les non-linéarités nécessaires pour classer les images.

7. **Analyse du graphique (diagramme d'un CNN appliqué à la classification d'image) :**
   - **YOUTBA3**



1. **Charger la base de données digits**
   ```python
   from sklearn.datasets import load_digits
   digits = load_digits()
   X = digits.data
   y = digits.target
   ```

2. **Séparer les données en 70% pour l'apprentissage et 30% pour le test**
   ```python
   from sklearn.model_selection import train_test_split
   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)
   ```

3. **Appliquer l'ACP pour réduire les dimensions à deux**
   ```python
   from sklearn.decomposition import PCA
   pca = PCA(n_components=2)
   X_train_pca = pca.fit_transform(X_train)
   X_test_pca = pca.transform(X_test)
   ```

4. **Créer un modèle KNN avec un voisinage K=3**
   ```python
   from sklearn.neighbors import KNeighborsClassifier
   knn = KNeighborsClassifier(n_neighbors=3)
   ```

5. **Ajuster le modèle sur l'ensemble d'apprentissage intégré (données transformées par PCA)**
   ```python
   knn.fit(X_train_pca, y_train)
   ```

6. **Calculer le score du KNN**
   ```python
   score = knn.score(X_test_pca, y_test)
   print(f"Le score de précision du modèle KNN sur les données de test est de {score:.2f}")
   ```

Ces étapes vous permettront de charger les données, de les préparer et de construire un modèle KNN après avoir réduit la dimensionnalité des données à l'aide de PCA. Vous pourrez ainsi évaluer la performance de votre modèle sur les données de test.

**@xDweb**