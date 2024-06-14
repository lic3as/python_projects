n = input('Digite algo: ')

ehLetra = n.isalpha()  #método para saber se é letra
ehNum = n.isnumeric()  #método para saber se é número
tipo = type(n)  #método para saber o tipo primitivo
ehAlfaNum = n.isalnum()  #método para saber se é alfanumérico, ou seja, letras e números
#existem várias outros métodos "is" para testar o que é alguma variável

print('{} é letra: {}'.format(n, ehLetra))
print('{} é número: {}'.format(n, ehNum))
print('{} é do tipo: {}'.format(n, tipo))
print('{} é alfanumérico: {}'.format(n, ehAlfaNum))
