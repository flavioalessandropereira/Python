cumprimento = "Olá, "
nome = "Flavio"
idade = 42
n_filhos  = 2

print (cumprimento + nome)

print(nome *5)

print(nome + ' tem ' + str(idade) + ' anos e ' + str (n_filhos) + " filhos.")

print ('{} tem {} anos e {} filhos'.format (nome, idade, n_filhos))


preco_gasolina = 5.999
print('O preço da gasolina hj está R$ {:.2f}'.format(preco_gasolina))

#usando o atalho format 
print(f'{nome} tem {idade} anos e {n_filhos} filhos')