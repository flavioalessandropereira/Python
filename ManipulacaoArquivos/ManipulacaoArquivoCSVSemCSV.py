with open('D:\GitHub\Python\ManipulacaoArquivos/brasil_covid.csv', 'r', encoding='utf-8') as csv_file:
    linhas = csv_file.read()
    linhas = linhas.split('\n')
    for linha in linhas:
        linha = linha.split(',')
        print(linha)