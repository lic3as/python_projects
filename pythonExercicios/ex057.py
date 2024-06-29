sexo = str(input('Informe seu sexo [F/M]: ')).strip().upper()[0]    # com o [0], ele lê somente a primeira letra informada

while sexo not in 'FM':                 # enquanto não digitar correto (F ou M), pedir novamente
    sexo = str(input('Dados inválidos. Informe seu sexo [F/M]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
