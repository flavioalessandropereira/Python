arquivo = open ('D:\GitHub\Python\ManipulacaoArquivos\domcasmurro.txt', 'r', encoding='utf-8')

for linha in arquivo:
    print(linha, end ='')

arquivo.close()