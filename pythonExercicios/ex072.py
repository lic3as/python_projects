extenso = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito',
           'nove', 'dez', 'onze', 'doze',
           'treze', 'catorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')
# tupla com todos os números de 0 a 20 por extenso

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:                                                          # se estiver netre 0 e 20
        print(f'Você digitou o número {extenso[num]}.')                         # apresentar a tupla na posição do número
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]     # se quer continuar
        if continuar == 'N':                                                    # se não quer continuar, para
            break
    else:                                                                       # se não estiver netre 0 e 20, tenta novamente
        print('Tente novamente.')
print('Fim do programa.')
