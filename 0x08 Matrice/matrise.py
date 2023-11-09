import numpy as np

# Define two matrices
N = np.array([[2, 4, 6],
              [4, 0, 10],
              [6, 10, 12]])

M = np.array([[1, 2, -6],
              [3, 4, 0],
              [3, 0, -3]])

dimension = N.shape[0]

I = np.eye(dimension)
# print(I)


somme = np.add(N, M)
NxM = np.dot(N, M)
MxN = np.dot(M, N)
IxM = np.dot(I, M)
MxI = np.dot(M, I)
M_transpose = M.T
M_transpose2 = np.transpose(M)
diagonal_M = M.diagonal()
diagonal_M2 = np.diag(M)

is_ident = np.array_equal(MxI, IxM)

# if is_ident:
#     print("La matrice M est une matrice identité.")
# else:
#     print("La matrice M n'est pas une matrice identité.")

#1
# print("Somme:")
# print(somme)



is_diagonal = np.all(M == np.diag(np.diagonal(M)))
print(np.diag(np.diagonal(M)))
if is_diagonal:
    print("La matrice M est diagonale.")
else:
    print("La matrice M n'est pas diagonale.")

# print(" N x M:")
# print(NxM)

# print(" M x N:")
# print(MxN)

# print(" I x M:")
# print(IxM)

# print(" M x I:")
# print(MxI)

result1 = (M + N).T

# # Calculez M^T + N^T
result2 = M.T + N.T

# # Comparez les deux résultats pour vérifier leur égalité
are_equal = np.array_equal(result1, result2)

# print("Résultat de (M + N)^T :")
# print(result1)

# print("Résultat de M^T + N^T :")
# print(result2)

# if are_equal:
#     print("(M + N)^T est égal à M^T + N^T.")
# else:
#     print("(M + N)^T n'est pas égal à M^T + N^T.")

# print(M_transpose)
# print(M_transpose2)

# print(diagonal_M)
# print(diagonal_M2)

is_M_symmetric = np.array_equal(M, M.T)

# if is_M_symmetric:
#     print("La matrice M est symétrique.")
# else:
#     print("La matrice M n'est pas symétrique.")

# is_N_symmetric = np.array_equal(N, N.T)

# if is_N_symmetric:
#     print("La matrice N est symétrique.")
# else:
#     print("La matrice N n'est pas symétrique.")

determinant_M = np.linalg.det(M)

# print("Déterminant de M :")
# print(determinant_M)
rang_M = np.linalg.matrix_rank(M)

# print("Rang de M :")
# print(rang_M)

trace_M = np.trace(M)

# print("Trace de M :")
# print(trace_M)