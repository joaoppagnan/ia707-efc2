import numpy as np
import scipy.io


def calc_custo_qap(solucao, distancias, fluxos):
    """
    Calcula o custo para um problema do tipo QAP
    :param solucao: solução que terá o custo calculado
    :param distancias: distância entre as localidades
    :param fluxos: fluxo entre as instalações
    :return: o custo de uma solução
    """
    n_items = fluxos.shape[0]
    custo = 0
    for i in range(0, n_items):
        for j in range(0, n_items):
            custo += distancias[i, j]*fluxos[solucao[0][i] - 1, solucao[0][j] - 1]
    return custo
