peso = float(input('Informe o seu peso em kg: '))
altura = float(input('Informe a sua altura em m: '))

imc = peso / (altura ** 2)              # imc = peso / altura²

if imc < 18.5:
    print('Seu IMC é de {:.1f}, você está ABAIXO DO PESO.'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é de {:.1f}, você está no PESO IDEAL.'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é de {:.1f}, você está com SOBREPESO.'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC é de {:.1f}, você está com OBESIDADE!'.format(imc))
elif imc >= 40:
    print('Seu IMC é de {:.1f}, você está com OBESIDADE MÓRBIDA. Cuidado!'.format(imc))
