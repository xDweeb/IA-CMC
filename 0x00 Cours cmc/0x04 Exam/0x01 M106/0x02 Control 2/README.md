### Partie 1 : questions de cours (8 points)

1. **Donne le nom de trois composants Talend appartenant à la phase Extraction (3 Points)** :
   - **tFileInputDelimited** : Permet de lire un fichier texte délimité.
   - **tFileInputExcel** : Permet de lire un fichier Excel.
   - **tMysqlInput** : Permet de lire des données d'une base de données MySQL.

2. **Donne le nom de trois composants Talend appartenant à la phase Transformation (3 Points)** :
   - **tFilterColumns** : Permet de filtrer les colonnes d'un flux de données.
   - **tConvertType** : Permet de convertir le type de données d'une colonne.
   - **tDenormalizeSortedRow** : Permet de dénormaliser les données.

3. **Donne le nom de trois composants Talend appartenant à la phase Chargement (3 Points)** :
   - **tMSSqlOutput** : Permet d'écrire des données dans une base de données SQL Server.
   - **tOracleOutput** : Permet d'écrire des données dans une base de données Oracle.
   - **tFileOutputDelimited** : Permet d'écrire des données dans un fichier texte délimité.

4. **Pourquoi on utilise le composant tLogRow ? (1 Point)**
   Le composant **tLogRow** est utilisé pour afficher le contenu des données traitées dans la console ou les logs, ce qui permet de vérifier et de déboguer les flux de données pendant l'exécution.

5. **Pourquoi on utilise le composant tFileOutputDelimited ? (1 Point)**
   Le composant **tFileOutputDelimited** est utilisé pour écrire des données dans un fichier texte délimité, permettant ainsi d'exporter et de sauvegarder les données traitées dans un format standardisé et facilement lisible par d'autres systèmes ou applications.

   ### Partie 2 : Liaison par flèche (5 points)

Lier chaque composant Talend avec son rôle.

1. **tFileInputDelimited**
   - Lecture d’un fichier CSV

2. **tUniqueRow**
   - Permet de détecter les lignes redondantes et de garder les lignes uniques

3. **tConvertType**
   - Transformer les données en modifiant leur type de données

4. **tFilterRow**
   - Sélectionner des lignes de données vérifiant des critères de sélection

5. **tMysqlOutput**
   - Charger un contenu dans une BD MySQL

Cela devrait vous aider à répondre aux questions correctement et à obtenir les points nécessaires.

### Partie 3 : Étude de cas (7 points)

Selon les phases Extraction, Transformation et Chargement de Talend, donnez le nom du composant Talend qui permet de :

1. **Lire le fichier délimité « Produits.csv » (0.5 Points)**
   - **tFileInputDelimited**

2. **Lire le fichier « Fournisseurs.xlsx » (0.5 Points)**
   - **tFileInputExcel**

3. **Convertir le type de Prix_Unitaire de string à Double (1 Point)**
   - **tConvertType**

4. **Faire une jointure des deux fichiers (1 Point)**
   - **tJoin**

5. **Faire une agrégation des Prix totaux des produits par Ville (1 Point)**
   - **tAggregateRow**

6. **Faire un tri ascendant par Prix totaux des produits (0.5 Points)**
   - **tSortRow**

7. **Faire un affichage des résultats sur la console sous forme de tableau (0.5 Points)**
   - **tLogRow**

8. **Dessiner le schéma complet du Job Talend (2 Points)**

   Voici un schéma simplifié du processus ETL à développer :

   1. **Extraction**
      - tFileInputDelimited (pour lire Produits.csv)
      - tFileInputExcel (pour lire Fournisseurs.xlsx)

   2. **Transformation**
      - tConvertType (pour convertir Prix_Unitaire de string à Double)
      - tJoin (pour faire la jointure des deux fichiers)
      - tAggregateRow (pour faire l'agrégation des prix totaux des produits par Ville)
      - tSortRow (pour trier par prix totaux des produits)

   3. **Chargement**
      - tLogRow (pour afficher les résultats sur la console)

   Le schéma visuel peut être représenté comme suit :

   ```
   tFileInputDelimited ----+
                           |
                           +----> tJoin ----> tAggregateRow ----> tSortRow ----> tLogRow
                           |
   tFileInputExcel --------+
   ```
