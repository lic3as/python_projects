frase = str(input('Digite uma frase: ')).strip().upper()        # já remover os espaços entre a string e funcionar sem case sensitive

print('A letra "A" aparece na frase {} vezes'.format(frase.count('A')))
print('A letra "A" aparece primeiro na posição [{}]'.format(frase.find('A')))
print('A letra "A" aparece por último na posição [{}]'.format(frase.rfind('A')))      # procurar a partir do lado direito (última ocorrência)
