from pickle import FALSE
import random

valor_aleatorio = random.randint(1, 10)


acertou = False

while acertou == False:
    chute = int(input('Chute um valor entre 1 a 10: '))
    if chute > valor_aleatorio:
        print('Chute maior que valor gerado')
    elif chute < valor_aleatorio:
        print('Chute menor que valor gerado')
    elif chute == valor_aleatorio:
        acertou = True
        print('Parabéns acertou')
