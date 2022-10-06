def notas(*nts, sit=False):
    """
    -> Função para o cálculo de notas dos alunos.
    :param nts: Contém as notas dos alunos.
    :param sit: (Opcional) Informa a situação com base na média das notas.
    :return: Retorna um dicionário com informações das notas.
    """
    media = sum(nts)/len(nts)
    if sit:
        if media >= 9:
            situ = 'Ótima'
        elif media >= 7:
            situ = 'Boa'
        elif media >= 5:
            situ = 'Razoável'
        else:
            situ = 'Ruim'
        return {'Total': len(nts), 'Maior': max(nts), 'Menor': min(nts), 'Média': media, 'Situação': situ}
    else:
        return {'Total': len(nts), 'Maior': max(nts), 'Menor': min(nts), 'Média': media}


# Programa Principal
resp = notas(3.5, 8, 7.6, sit=True)
print(resp)
