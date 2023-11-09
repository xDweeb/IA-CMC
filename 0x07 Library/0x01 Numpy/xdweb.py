#Créer un tableau unidimensionnel NumPy à partir des listes Python

import numpy as xdweb
a=xdweb.random.randint(10,size=(2,4,3))
a[0,1,-1]=7
print(a)