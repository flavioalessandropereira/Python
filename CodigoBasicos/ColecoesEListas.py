precos = [20, 50, 200]

print('o valor do index 1 = ', precos[1])
print('index do preço 200 = ', precos.index(200))

diversidades = [23, 'flavio', True]
print(diversidades[0])
print(diversidades[1])
print(diversidades[2])

for preco in precos:
    print(preco)

# soma valores [15, 46, 75,23, 34]
idades = [15, 46, 75, 23, 34]
total = 0

for idade in idades:
    total = total + idade
print('a somatória da lista de idades = ', total)
