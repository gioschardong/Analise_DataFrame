# Imports
import requests
import pandas as pd

pd.set_option('mode.chained_assignment', None)


# Função para Baixar o arquivo
def baixar_arquivo(url, endereco):
    # Faz requisição
    resposta = requests.get(url)

    # Verifica se Deu certo
    if resposta.status_code == requests.codes.OK:
        with open(endereco, 'wb') as novo_arquivo:
            novo_arquivo.write(resposta.content)
        print()
        print("Download realizado com sucesso. Salvo como: {}".format(endereco))
        print()
    else:
        resposta.raise_for_status()

# Função para Testar valor do ano
def testaNum(ano):
    if (ano >= 1997 and ano <= 2022):
        return True
    else:
        return False

# Função para analizar e imprimir dados
def analizar_arquivo(endereco, ano):
    # Leitor do arquivo
    df = pd.read_csv(endereco, sep=";")

    # Filtro Informações
    df_ano = df.loc[df['ANO'] == ano]

    # Trocar "," por "." e converte em float
    df_ano['PRODUÇÃO'] = df_ano['PRODUÇÃO'].apply(
        lambda x: float(x.replace(",", ".")))

    # Soma
    total = df_ano['PRODUÇÃO'].sum()

    return total

# Função para imprimir o resultado
def imprime(conteudo):
    # print(df_ano)
    print()
    print("A quantidade produzida de petróleo no ano foi de: ", end='')
    print(conteudo, end='')
    print(" m³")
    print()


if __name__ == "__main__":
    baixar_arquivo(
        'https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/ppgn-el/producao-petroleo-m3-1997-2022.csv', 'dados.csv')
    anoString = input("Escolha o ano (entre 1997 e 2022) a ser analisado: ")
    ano = int(anoString)
    teste = testaNum(ano)
    if (teste):
        resultado = analizar_arquivo('dados.csv', ano)
        imprime(resultado)
    else:
        print("O ano de ", end='')
        print(ano, end='')
        print(" não é valido")
