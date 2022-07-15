dados_cidades = {
    'nome' : 'São Paulo',
    'estado' : 'São Paulo',
    'area_km2' : 1521,
    'populacao_milhoes' : 12.18
}
print(type(dados_cidades)) #ver tipo de variavel

print(dados_cidades)

#adicionar outra informação no dicionário
dados_cidades['pais'] = 'Brasil'
print (dados_cidades)

print(dados_cidades['estado'])

#alterar dados dentro de um dicionario
dados_cidades['area_km2'] = 1.4
print (dados_cidades)


# criando outro dicionario e caso mude um o outro tb será mudado
dados_cidade2 = dados_cidades
dados_cidade2['nome'] = 'Santos'
print(dados_cidades)
print(dados_cidade2)

#usando o comando copy ao copiar um dicionario, qdo alterar alguma informação somente um será alterado
dados_cidade3 = dados_cidades.copy()
dados_cidade3['estado'] = 'Rio de Janeiro'
print (dados_cidades)
print(dados_cidade3)

#adicionar novas informações no dicionario
novos_dados = {
    'populacoa_milhoes':15,
    'fundacao' : '25/01/1554'

}
dados_cidades.update(novos_dados)
print (dados_cidades)

#acessar uma chave usando o GET
print(dados_cidades.get('prefeito'))

#retorna uma lista de chaves de um dicionario
print(dados_cidades.keys())

#retorna uma lista de valores de um dicionário
print(dados_cidades.values())

#retorna uma lista de tuplas (chave, valor) de um dicionario
print(dados_cidades.items())