import random

def gera_img():
    imagem = [(0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0)]
    for _ in range(1000):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        imagem.append((r,g,b))
    random.shuffle(imagem)
    return imagem

def media_pixel(imagem):
    media = []
    pretos = 0
    for pixel in imagem:
        calculo = round(abs((pixel[0] + pixel[1] + pixel[2])/3), 1)
        media.append(calculo)
        if calculo == 0:
            pretos+=1
    return (f" {media} \nQuantidade de pixels pretos: {pretos}")

print(media_pixel(gera_img()))