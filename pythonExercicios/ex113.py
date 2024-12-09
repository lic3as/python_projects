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


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (TypeError, ValueError):
            print(f"\033[0;31mERRO! Digite um número real válido.\033[m")
        except KeyboardInterrupt:
            print(f"\033[0;31mEntrada de dados interrompida pelo usuário.\033[m")
            return 0
        else:
            break
    return n


n1 = leiaInt("Digite um inteiro: ")
n2 = leiaFloat("Digite um real: ")

print(f"O valor inteiro digitado foi {n1} e o real foi {n2}.")
