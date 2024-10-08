nome = str(input('Nome: '))                     # recebe o nome
media = float(input(f'Média de {nome}: '))      # recebe a média
if media >= 7:                                  # processa a situação
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado'

pessoa = {'Nome': nome, 'Média': media, 'Situação': situacao}   # adiciona tudo ao dicionário pessoa

for k, v in pessoa.items():
    print(f'-- {k} é igual a {v}')
# imprimir key e value
