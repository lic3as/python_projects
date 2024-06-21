print('\033[1;31;43mOlá, Mundo!\033[m')        # formatar cores
# comando \033[STYLE;FOREGROUND;BACKGROUNDm     ->      ver a tabela com o código dos estilos, cores de texto e cores de fundo e colocar
# STYLE: 0 - none; 1 - bold; 4 - underline; 7 - negative
# TEXT : 30, 31, 32, 33, 34, 35, 36, 37
# BACK: 40, 41, 42, 43, 44, 45, 46, 47
# text e back possuem as mesma cores só mudam os códigos
print('\33[4;30;45mTudo bem?\033[m')
print('\033[7;30;45m:)\033[m')
nome = str(input('Qual o seu \033[34mnome\033[m e o seu \033[32msobrenome\033[m? '))
print('É um prazer \033[4;41m{}\033[m!'.format(nome))
