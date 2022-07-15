import csv

with open('D:\GitHub\Python\ManipulacaoArquivos/brasil_covid.csv', 'r', encoding='utf-8') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    header =next(leitor)
    for linha in leitor:
        if float (linha[2]) > 1: # verificar na posição "novos_casos" > 1 e ignorar o 'novos_casos
            print(linha)