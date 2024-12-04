def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


#soma(8, 9)
#soma(5, 2)
#soma(b=11, a=3)         # dá pra trocar a posição dos valores, se vc especificar


def contador(* num):    # com o asterisco antes do parâmetro, vc informa q não sabe a quantidade parâmetros q serão passados, o python criará uma tupla com todos eles
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')


#contador(7, 0, 10, 21, 4)
#contador(1, 2, 3)
#contador(10, 2, 6, 4, 9, 0, 1, 3)


def somaValores(* valores):
    total = 0
    for v in valores:
        total += v
    print(f'Somando os valores {valores}, o resultado é {total}.')


somaValores(1, 2, 3, 4, 5, 6)
somaValores(9, 8, 2, 1)
