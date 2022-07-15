with open('arquivo_teste.txt', 'w' , encoding='utf-8') as arquivo:
    arquivo.write('Esse é somente um teste\n')
    arquivo.write('Essa é a segunda linha .. sera? \n')

with open('arquivo_teste.txt', 'r' , encoding='utf-8') as arquivo:
    print(arquivo.read(), end='')

with open('arquivo_teste.txt', 'a' , encoding='utf-8') as arquivo:
    arquivo.write('Essa é a tereceira linha de teste\n')
    
with open('arquivo_teste.txt', 'r' , encoding='utf-8') as arquivo:
    print(arquivo.read(), end='')
