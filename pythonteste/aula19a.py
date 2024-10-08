pessoas = { 'nome' : 'Alice', 'sexo': 'F', 'idade': '21'}
print(pessoas['nome'])

# em dicionários, usamos {}, além disso, as posições são identificadas por nomes (nome, sexo, idade)
# ou seja, quando for dar print, tem que fazer o nome da posição dentro do dicionário

print(f'A {pessoas["nome"]} tem {pessoas["idade"]} anos.')

# pra fazer um print formatado, como já usamos aspas nas fstrings, utilizamos aspas duplas pra indiciar a posição no dicionário
# keys é o nome das posições
#print(pessoas.keys())
# value é o que está contido em cada key
#print(pessoas.values())
# item é o key e o value
#print(pessoas.items())

# eu posso usar isso em laços pra mostrar cada posição do dicionário
#for k, v in pessoas.items():
#    print(f'{k} = {v}') # key = value pra cada repetição

# eu posso usar o comando del pra apagar alguma key do dicionário
# não precisa dar append pra adicionar algo
pessoas["peso"] = 64.2

for k, v in pessoas.items():
    print(f'{k} = {v}') # key = value pra cada repetição

