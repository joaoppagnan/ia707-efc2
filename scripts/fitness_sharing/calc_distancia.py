import numpy as np


def calc_distancia(individuo_i: np.ndarray, individuo_j: np.ndarray):
    """
    Calcula a distância entre o indivíduo i e o indivíduo j
    :param individuo_i: Primeiro indivíduo para o cálculo da distância
    :param individuo_j: Segundo indivíduo para o cálculo da distância
    :return: Distância entre os indivíduos
    """
    distancia = np.sqrt((individuo_i[0] - individuo_j[0])**2 + (individuo_i[1] - individuo_j[1])**2)
    return distancia
