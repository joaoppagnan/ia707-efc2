import numpy as np
import scipy.io
from calc_custo_qap import calc_custo_qap


CUSTO_OTIMO = 17212548


def calc_fitness_qap(solucoes, distancias, fluxos):
    """
    Calcula o fitness para um problema do tipo QAP
    :param solucoes: solucoes que terão o fitness calculado
    :param distancias: distância entre as localidades
    :param fluxos: fluxo entre as instalações
    :return: o conjunto de soluões com o fitness atualizado
    """
    for solucao in solucoes:
        if solucao[1] == 0:
            custo = calc_custo_qap(solucao=solucao, distancias=distancias, fluxos=fluxos)
            fitness = (1/custo)/(1/CUSTO_OTIMO)
            solucao[1] = fitness
            solucao[2] = custo
    return solucoes
