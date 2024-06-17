from math import sqrt, ceil     # importando os métodos sqrt e ceil da biblioteca math - forma mais específica, economia de espaço
#import math     # importando a biblioteca math (todas as suas funcionalidades - forma mais generalizada)

num = int(input('Digite um número: '))

raiz = sqrt(num)   # agora, quando digitar "math." já aparecem todos os métodos de math, sqrt é a raiz quadrada

print('A raiz de {} é igual a {:.2f}'.format(num, ceil(raiz)))     # ceil mostra o arredondamento pra cima, floor arredonda pra baixo
# o :.2f faz com que o número seja formatado com 2 casas após a vírgula
# ir no pypi para importar pacotes separadamente
