import numpy as np


def recombinacao_crossover_aritmetico(cromossomo_p1, cromossomo_p2):
    """
    Realiza a recombinação crossover aritmético com dois cromossomos
    :param np.ndarray cromossomo_p1: cromossomo do pai 1
    :param np.ndarray cromossomo_p2: cromossomo do pai 2
    :return: dois descendentes
    """
    descendentes = []
    a = np.random.uniform(low=0, high=1)
    for i in range(0, 2):
        cromossomo_filho = []
        for j in range(0, 2):
            if i == 0:
                cromossomo_filho.append(a*cromossomo_p1[j] + (1 - a)*cromossomo_p2[j])
            elif i == 1:
                cromossomo_filho.append((1 - a)*cromossomo_p1[j] + a*cromossomo_p2[j])
        descendentes.append([cromossomo_filho, 0])
    return descendentes
