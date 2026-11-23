import random

def gera_posicao(n):
    posicoes = []
    for _ in range (n):
        x = (random.randint(0,100))
        y = (random.randint(0,100))
        raio = (random.randint(2,10))
        posicoes.append((x,y,raio))
    if n > 1:
        return posicoes
    else:
        return (x, y, raio)

def colisao(obstaculos, jogador):
    colisoes = 0
    for obstaculo in obstaculos:
        distancia = abs(jogador[0]-obstaculo[0]) + abs(jogador[1]-obstaculo[1])
        raio = jogador[2] + obstaculo [2]
        if distancia <= raio:
            colisoes += 1
    if colisoes > 0:
        return (True, colisoes)
    else:
        return (False, colisoes)

# Jeito legal =
# resultado = (colisao(gera_posicao(int(input("Quantos obstaculos? "))), gera_posicao(1)))

# Jeito chato =
resultado = colisao([(12,4,3),(34,15,5),(89,43,6),(67,90,8),(34,56,9),(28,55,10)],(30,55,8))

if resultado[0] == True:
    print(f"Impacto Detectado! \nObjetos atingidos: {resultado[1]}")
else:
    print(f"Caminho livre \nObjetos atingidos: {resultado[1]}")