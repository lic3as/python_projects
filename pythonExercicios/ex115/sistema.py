from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arquivo = "pessoas.txt"

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    opcao = menu(["Ver pessoas cadastradas;", "Cadastrar nova pessoa;", "Sair do sistema."])
    if opcao == 1:
        lerArquivo(arquivo)
    elif opcao == 2:
        cabecalho("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = leiaInt("Idade: ")
        cadastrar(arquivo, nome, idade)
    elif opcao == 3:
        cabecalho("Saindo do sistema... até logo!")
        break
    else:
        print(f"\033[0;31mERRO! Digite um opção válida.\033[m")
    sleep(2)

