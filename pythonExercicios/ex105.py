def notas(*n, sit=False):
    """
    — > Função para analisar notas e situação de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: opcional, indica se quer ou não ver a situação (True or False).
    :return: dicionário com as informações sobre a situação da turma.
    """
    result = dict()
    result["total"] = len(n)
    result["maior"] = max(n)
    result["menor"] = min(n)
    result["média"] = sum(n)/len(n)
    if sit:
        if result["média"] < 6:
            result["situação"] = "RUIM"
        elif result["média"] < 7:
            result["situação"] = "RAZOÁVEL"
        elif result["média"] < 9:
            result["situação"] = "BOA"
        else:
            result["situação"] = "EXCELENTE"
    return result


r = notas(9, 7.5, 10, 9.8, sit=True)
print(r)
help(notas)
