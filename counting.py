def contar():
    nome_arquivo = 'dados.txt'
    try:
        numlin = 0
        numpal = 0
        numcar = 0
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:

            for linha in arquivo:
                numlin += 1
                numcar += len(linha)
                palavrasplinha = linha.split()
                numpal += len(palavrasplinha)
        print(f"Número de linhas: {numlin}")
        print(f"Número de palavras: {numpal}")
        print(f"Número de caracteres: {numcar}")
    except Exception as e:
        print(f"O seguinte erro ocorreu: {e}")
contar()