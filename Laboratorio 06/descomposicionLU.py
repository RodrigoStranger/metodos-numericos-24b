def LU(A):
    n = len(A)
    # inicializamos L como una matriz identidad
    L = [[0.0 if i != j else 1.0 for j in range(n)] for i in range(n)]
    # inicializamos U como una copia de la matriz A
    U = [row[:] for row in A]
    # aplicamos la eliminación de Gauss
    for i in range(n):
        for j in range(i + 1, n):
            # calculamos el factor f_ij
            factor = U[j][i] / U[i][i]
            L[j][i] = factor 
            # actualizamos la fila j de U restando el múltiplo de la fila i
            for k in range(i, n):
                U[j][k] -= factor * U[i][k]
    return L, U

MatrizOriginal = [
    [1, 2, 3],
    [4, 5, -2],
    [2, 1, 3]
]

L, U = LU(MatrizOriginal)

print("Matriz original:")
for fila in MatrizOriginal:
    print(fila)

print(" ")

print("Matriz U:")
for fila in U:
    print(fila)

print(" ")

print("Matriz L:")
for fila in L:
    print(fila)
