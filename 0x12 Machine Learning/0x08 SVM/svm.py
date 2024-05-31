#SVM-GPT
# Importer les bibliothèques nécessaires
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix

# Charger les données à partir du fichier CSV
data = pd.read_csv('bill_authentication.csv')

# Diviser les caractéristiques et les étiquettes
X = data.drop('Class', axis=1)  # Les caractéristiques sont toutes les colonnes sauf 'Class'
y = data['Class']  # 'Class' est notre étiquette

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialiser le classificateur SVM
classifier = SVC(kernel='linear', random_state=42)

# Entraîner le modèle SVM
classifier.fit(X_train, y_train)

# Prédire les étiquettes pour l'ensemble de test
y_pred = classifier.predict(X_test)

# Calculer la matrice de confusion
conf_matrix = confusion_matrix(y_test, y_pred)
print("Matrice de confusion :\n", conf_matrix)


#SVM-CLASS
# استيراد الدالة classification_report من مكتبة sklearn
from sklearn.metrics import classification_report

# طباعة تقرير التصنيف باستعمال القيم الحقيقية y_test والتوقعات y_pred
print(classification_report(y_test, y_pred))

# استيراد مكتبة numpy لتعمل على المصفوفات والحسابات العددية
import numpy as np

# استيراد مكتبة pandas لقراءة البيانات على شكل جداول
import pandas as pd

# لم يتم استخدام matplotlib.pyplot في هذا الكود، لذلك لا داعي لاستيراده
# import matplotlib.pyplot as plt

# استيراد الدالة train_test_split من مكتبة sklearn لتقسيم البيانات لتدريب واختبار النموذج
from sklearn.model_selection import train_test_split

# استيراد مكتبة SVC من sklearn لبناء نموذج SVM
from sklearn.svm import SVC

# استيراد الدالة confusion_matrix من مكتبة sklearn لحساب مصفوفة الالتباس
from sklearn.metrics import confusion_matrix

# قراءة البيانات من ملف CSV باستخدام pandas
data = pd.read_csv('bill_authentication.csv')

# تقسيم البيانات X و y لجزء التدريب وجزء الاختبار باستخدام train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# إنشاء نموذج SVM
Classifier = SVC(kernel='linear', random_state=0)

# تدريب النموذج باستخدام بيانات التدريب
Classifier.fit(X_train, y_train)

# التنبؤ بالقيم y باستخدام النموذج المدرب على بيانات الاختبار
y_pred = Classifier.predict(X_test)

# حساب مصفوفة الالتباس باستخدام القيم الحقيقية والتوقعات
cm = confusion_matrix(y_test, y_pred)

# استيراد الدالة classification_report من مكتبة sklearn لطباعة تقرير التصنيف
from sklearn.metrics import classification_report

# طباعة تقرير التصنيف باستخدام القيم الحقيقية والتوقعات
print(classification_report(y_test, y_pred))


#code-svm-gpt
# Importer les bibliothèques nécessaires
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Chargement des données (vous pouvez utiliser un autre jeu de données si nécessaire)
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardiser les caractéristiques en retirant la moyenne et en mettant à l'échelle la variance unitaire
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Initialiser le classificateur SVM
classifier = SVC(kernel='linear', random_state=42)

# Entraîner le modèle SVM
classifier.fit(X_train, y_train)

# Prédire les étiquettes pour l'ensemble de test
y_pred = classifier.predict(X_test)

# Calculer la précision du modèle
accuracy = accuracy_score(y_test, y_pred)
print("Précision du modèle SVM : {:.2f}%".format(accuracy * 100))
