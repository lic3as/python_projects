num = qtd = media = 0

while True:                     # loop infinito
    num = int(input('Digite um número [-1 para parar]: '))
    if num == -1:               # condição de parada = -1
        break
    else:
        qtd += 1                # incrementar a quantidade
        media += num            # adicionar a média
media /= qtd                    # dividir a soma pela quantidade pra obter a média

print(f'Você digitou {qtd} números e a média entre eles foi {media:.2f}.')
# atualização f strings, agora, invés de .format é só colocar f no começo da string e as variáveis dentro das chaves
