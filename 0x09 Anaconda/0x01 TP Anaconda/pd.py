import pandas as pd
datacsv = 'C:/Users/GM4/Documents/data/data.csv'
# 1. Lire le fichier CSV
data = pd.read_csv(datacsv)

# 2. Afficher les cinq premières lignes
print("Les cinq premières lignes :")
print(data.head())

# 3. Afficher toutes les informations du dataframe
print("\nInformations du dataframe :")
print(data.info())

# 4. Afficher le nom des colonnes
print("\nNoms des colonnes :")
print(data.columns)

# 5. Afficher le type des données
print("\nTypes de données :")
print(data.dtypes)

# 6. Afficher le nombre de valeurs manquantes
print("\nNombre de valeurs manquantes par colonne :")
print(data.isnull().sum())

# 7. Nettoyer les données (par exemple, remplacer les valeurs manquantes par la moyenne)
data_cleaned = data.fillna(data.mean())

# 8. Afficher les statistiques descriptives
print("\nStatistiques descriptives :")
print(data_cleaned.describe())