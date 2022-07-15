
def calcula_media(*args, margem):  # args = variável e adcionar marge 0.3
    soma = sum(args)
    media = soma / len(args)
    print(media)
    return media + margem
    


calcula_media(10, 8, 9, margem = 0.3)

