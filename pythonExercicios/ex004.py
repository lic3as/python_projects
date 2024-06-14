text = input('Digite algo: ')

print('O tipo primitivo desse valor é', type(text))  #método para saber o tipo
print('Só tem espaços?', text.isspace())  #método para saber se só tem espaços
print('É um número?', text.isnumeric())  #método para saber se é um número
print('É alfabético?', text.isalpha())  #método para saber se é uma letra
print('É alfanumérico?', text.isalnum())  #método para saber se são letras e números
print('Está em maiúsculas?', text.isupper())  #método para saber se está tudo em maiúsculo
print('Está em minúsculas?', text.islower())  #método para saber se está tudo em minúsuculo
print('Está capitalizado?', text.istitle())  #método para saber se está capitalizado - começando com maiúscula
