import csv

# cria arquivo csv e newline='' retira uma quebra de linha
with open('users.csv', 'w', encoding='utf8', newline='')as arquivo_users:
    escritor = csv.writer(arquivo_users)
    escritor.writerow(['nome', 'sobrenome', 'email', 'gernero'])
    escritor.writerow(
        ['Flavio', 'Pereira', 'flavioapereira@yahoo.com.br', 'Masculino'])
