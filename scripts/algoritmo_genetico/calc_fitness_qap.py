import numpy as np
import scipy.io
from calc_custo_qap import calc_custo_qap


CUSTO_OTIMO = 17212548


def calc_fitness_qap(populacao, distancias, fluxos):
    """
    Calcula o fitness para um problema do tipo QAP
    :param populacao: populacao que terá o fitness calculado
    :param distancias: distância entre as localidades
    :param fluxos: fluxo entre as instalações
    :return: a população com o fitness atualizado
    """
    for individuo in populacao:
        if individuo[1] == 0:
            custo = calc_custo_qap(individuo=individuo, distancias=distancias, fluxos=fluxos)
            fitness = (1/custo)/(1/CUSTO_OTIMO)
            individuo[1] = fitness
            individuo[2] = custo
    return populacao
