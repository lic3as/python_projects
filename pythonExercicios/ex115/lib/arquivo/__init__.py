from ex115.lib.interface import *


def arquivoExiste(arq):
    try:
        a = open(arq, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(arq):
    try:
        a = open(arq, "wt+")
        a.close()
    except:
        print("\033[0;31mHouve um erro na criação do arquivo!\033[m")
    else:
        print(f"\033[32mArquivo {arq} criado com sucesso!\033[m")


def lerArquivo(arq):
    try:
        a = open(arq, "rt")
    except:
        print("\033[0;31mErro ao ler o arquivo!\033[m")
    else:
        cabecalho("PESSOAS CADASTRADAS")
        for linha in a:
            dado = linha.split(";")
            dado[1] = dado[1].replace("\n", "")
            print(f"{dado[0]:<30} {dado[1]:>3} anos")
    finally:
        a.close()


def cadastrar(arq, n="desconhecido", i=0):
    try:
        a = open(arq, "at")
    except:
        print("\033[0;31mHouve um erro na abertura do arquivo!\033[m")
    else:
        try:
            a.write(f"{n};{i}\n")
        except:
            print("\033[0;31mHouve um erro na hora de escrever os dados!\033[m")
        else:
            print(f"\033[32mNovo registro de {n} adicionado.\033[m")
            a.close()
