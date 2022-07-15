#criar uma função tem a palava reservada DEF
def hello():
    print('Olá mundo')

hello()

#função de calcular média
def calcular_media(valor1, valor2, valor3):
    media = (valor1+valor2+valor3)/3
    return media

resultado = calcular_media(10,50,30)
print(resultado)

resultado2 = calcular_media(valor1=9, valor2=20, valor3=30)
print(resultado2)

#função recursiva
def funcaoRecursiva(numero):
    if (numero != 1):
        funcaoRecursiva(numero - 1)
    print(numero)

print("Testando a função recursiva:")
funcaoRecursiva(10)

# função com resposta
def somatorio(lista):
    soma = 0
    for item in lista:
        soma = soma + item
    return soma

numeros = [1, 2, 3, 4, 5]
soma_dos_numeros = somatorio(numeros)
print("A soma dos elementos da lista vale: ", soma_dos_numeros)

if somatorio(numeros) > 50:
    print("Que soma grande!")
else:
    print("Que soma pequena!")


#função com parâmetros
def dadosPessoais(nome, idade, cidade):
    print("Seu nome é {}, você tem {} anos e mora em {}.".format(nome, idade, cidade))

dadosPessoais("José", 30, "Maceió")

dadosPessoais(idade=56, cidade="Florianópolis", nome="Ana")