import numpy as np
import scipy.io


def calc_custo_qap(individuo, distancias, fluxos):
    """
    Calcula o custo para um problema do tipo QAP
    :param individuo: solução que terá o custo calculado
    :param distancias: distância entre as localidades
    :param fluxos: fluxo entre as instalações
    :return: o custo de uma solução
    """
    n_alelos = fluxos.shape[0]
    custo = 0
    for i in range(0, n_alelos):
        for j in range(0, n_alelos):
            custo += distancias[i, j]*fluxos[individuo[0][i] - 1, individuo[0][j] - 1]
    return custo
