import numpy as np # type: ignore

a = np.array([3, 4])
b = np.array([1, 2])

# Penjumlahan
c = a + b
print("Penjumlahan:", c)

# Perkalian skalar
k = 2 * a
print("Perkalian skalar:", k)

# Dot product
dot_product = np.dot(a, b)
print("Dot Product:", dot_product)

# Norma vektor
norm_a = np.linalg.norm(a)
print("Norma Vektor a: ", norm_a)