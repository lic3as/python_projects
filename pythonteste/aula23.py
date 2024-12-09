try:                # tenta executar
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
except (ValueError, TypeError):     # se der problema de valor ou tipo
    print("Tivemos um problema com os tipos de dados que você informou.")
except ZeroDivisionError:           # se der problema de divisão por zero
    print("Não é possível dividir por zero.")
except KeyboardInterrupt:           # se parar de informar no teclado
    print("O usuário não informou os valores.")
except Exception as erro:           # ver qual foi o erro, serve pros testes
    print(f"O erro encontrado foi {erro.__class__}")
else:                               # se não deu problema
    print(f"O resultado é {r:.2f}.")
finally:                            # executa independente de ter dado problema ou não
    print("Volte sempre! Muito obrigada!")
