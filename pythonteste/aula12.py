nome = str(input('Digite o seu nome: '))

if nome == 'Alice':                                                             # se o nome é igual a alice, imprime isso
    print('Que nome mais lindo!')
elif nome == 'Maria' or nome == 'José' or nome == 'Pedro' or nome == 'Ana':     # senão, se o nome é igual a maria, josé, pedro ou ana, imprime isso
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Clara Lívia Aurora Luiza':                                        # senão, se for um dos nomes listados, imprime isso
    print('É um belo nome feminino.')
elif nome in 'Michael Arthur Antony Ravi':                                      # senão, se for um dos nomes listados, imprime isso
    print('É um belo nome masculino.')
else:                                                                           # senão, imprime isso
    print('É um nome bem normal.')
# estrutura condicional aninhada: if - se; elif - senão, se; else - senão
print('Tenha um bom dia, {}!'.format(nome))                                     # não entra na condição porque não está identado
