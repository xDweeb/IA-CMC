import numpy as np

# Définir la matrice A et le vecteur colonne Y
A = np.array([[1, 5, 9], [9, 10, 5], [10, 9, 1]])
Y = np.array([[180], [40], [-50]])

# Utiliser la fonction solve de NumPy pour résoudre le système
X = np.linalg.solve(A, Y)

# Afficher la solution
print("La solution du système est :")
print("x1 =", X[0, 0])
print("x2 =", X[1, 0])
print("x3 =", X[2, 0])






# import numpy as np

# # Définir la matrice A
# A = np.array([[2, 2, -3],
#               [-2, -1, -3],
#               [6, 4, 4]])

# # Définir le vecteur Y
# Y = np.array([[-14],
#               [21],
#               [4]])

# # Calculer l'inverse de la matrice A
# A_inverse = np.linalg.inv(A)

# # Calculer le vecteur X en multipliant l'inverse de A par Y
# X = np.dot(A_inverse, Y)

# # Afficher la solution
# print("La solution du système d'équations est :\n", X)
