# abre e fecha o arquivo automaticamente
with open ('D:\GitHub\Python\ManipulacaoArquivos\domcasmurro.txt', 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()
    print(texto)