import numpy as np

notas = np.array([5.5, 8.0, 4.5, 9.0, 6.5])

notas2 = np.insert(notas, 2, 7)
print(notas2)

mascara = notas2 < 6
notas2[mascara] = 6
print(notas2)

notas2 = np.delete(notas2, 4)
print(notas2)