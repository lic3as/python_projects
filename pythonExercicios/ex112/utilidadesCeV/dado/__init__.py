def leiaDinheiro(msg):
    ok = False
    while True:
        dinheiro = str(input(msg)).replace(',', '.').strip()
        if dinheiro.isalpha() or dinheiro == '':
            print(f'\033[0;31mERRO: "{dinheiro}" é um preço inválido!\033[m')
        else:
            dinheiro = float(dinheiro)
            ok = True
        if ok:
            break
    return dinheiro
