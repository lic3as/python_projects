def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print(f"\033[0;31mERRO! Digite um número inteiro válido.\033[m")
        except KeyboardInterrupt:
            print(f"\033[0;31mEntrada de dados interrompida pelo usuário.\033[m")
            return 0
        else:
            break
    return n


def linha(tam=42):
    print("-" * (tam + 2))


def cabecalho(msg):
    linha()
    print(msg.center(44))
    linha()


def menu(lista):
    cabecalho("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print(f"\033[33m{c}\033[m - \033[34m{item}\033[m")
        c += 1
    linha()
    opc = leiaInt("\033[32mInforme sua opção: \033[m")
    return opc

