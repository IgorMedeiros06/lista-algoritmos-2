import numpy as np

notas = np.array([
    [5.0, 7.5, 6.0],
    [8.0, 9.0, 4.0],
    [3.5, 5.0, 6.5],
    [7.0, 6.0, 8.5]
])

print(f"Média dos alunos: {np.mean(notas, axis=1)}")


media_avaliacao = np.mean(notas, axis=0)
print(f"Maior média foi da avaliação {np.argmax(media_avaliacao)+1}")

nota_menor6 = notas < 6
notas[nota_menor6] = 6
print(notas)

notas_atualizada = np.delete(notas, 2, axis=1)
print(notas_atualizada)