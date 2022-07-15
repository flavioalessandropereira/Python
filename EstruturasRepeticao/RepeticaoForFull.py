nomes_cidades = ['São Paulo', 'Londres','Toquio','Paris']

#laço repeticao For
for nome in nomes_cidades:
    print(nome)

#laço repeticao usando While
contador = 0
nomes_cidades = ['São Paulo', 'Londres','Toquio','Paris']
while contador < len(nomes_cidades):
    print(nomes_cidades[contador])
    contador +=1

# usando como TUPLA
nomes_cidades1 = 'São Paulo', 'Londres','Toquio','Paris'
for nome in nomes_cidades1:
    print(nome)

#usando como dicionario
cidade = {
    'nome': 'São Paulo',
    'estado': 'São Paulo',
    'populacao_milhoes' : 12.2
}
for chave in cidade:
    print(f'{chave}:  {cidade[chave]}')


#alterar todos os elementos
for posicao in range(len(nomes_cidades)):
    nomes_cidades[posicao] = "rio de janeiro"
print (nomes_cidades)

print(list(range(10)))

print(list(range(2,10)))

print(list(range(2,10,2)))