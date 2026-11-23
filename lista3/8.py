import numpy as np

# def matriz4x4 ():
#     matriz = np.empty((0,4), dtype=int)
#     for _ in range (4):
#         array = np.array([])
#         for _ in range (4):
#             array = np.append(array,(np.random.randint(10,99)))
#         matriz = np.vstack((matriz, array))
#     return matriz.astype(int)

def matriz4x4():
    matriz = np.random.randint(10, 100, size=(4,4))
    return matriz

matriz = matriz4x4()
print(matriz)

somas = np.sum(matriz, axis=1)
medias = np.mean(matriz, axis=0)

print("somas:", somas)
print("medias:", medias)