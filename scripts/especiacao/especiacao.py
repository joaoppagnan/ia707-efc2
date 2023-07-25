import numpy as np
from calc_distancia import calc_distancia


def especiacao(individuo_1: np.ndarray, individuo_2: np.ndarray, sigma_mate: float):
    """
    Checa se a recombinação pode ser realizada entre os indivíduos
    :param individuo_1: cromossomo do pai 1
    :param individuo_2: cromossomo do pai 2
    :param sigma_mate: distância máxima entre indivíduos
    :return: um valor booleano que diz se ela pode ser realizada
    """
    distancia = calc_distancia(individuo_1[0], individuo_2[0])
    if distancia < sigma_mate:
        return True
    elif distancia == 0.0:
        return False
    else:
        return False
