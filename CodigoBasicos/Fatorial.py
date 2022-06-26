valor = int(input('Digite um numero a ser fatoriado: '))
fatorial = 1

if valor > 0:
    for item in range(1, valor + 1):
        fatorial = fatorial * item
    print('O fatorial de ', valor, ' = ', fatorial)
