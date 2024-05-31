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

