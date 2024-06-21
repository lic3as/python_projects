from datetime import date

print('-=-'*20)
print('Confederação Nacional de Natação')
print('-=-'*20)

nasc = int(input('Informe o ano do seu nascimento: '))
idade = date.today().year - nasc

print('A sua idade é de {} anos.'.format(idade))
if idade <= 9:
    print('Você se enquadra na categoria MIRIM de natação.')
elif idade <= 14:
    print('Você se enquadra na categoria INFANTIL de natação.')
elif idade <= 19:
    print('Você se enquadra na categoria JÚNIOR de natação.')
elif idade <= 20:
    print('Você se enquadra na categoria SÊNIOR de natação.')
else:
    print('Você se enquadra na categoria MASTER de natação.')
