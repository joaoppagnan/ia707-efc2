import numpy as np
import scipy.io


def calc_fitness(populacao):
    """
    Calcula o fitness
    :param populacao: populacao que terá o fitness calculado
    :return: a população com o fitness atualizado
    """
    for individuo in populacao:
        if individuo[1] == 0:
            x = individuo[0][0]
            y = individuo[0][1]
            fitness = x*np.sin(4*np.pi*x) - y*np.sin(4*np.pi*y + np.pi) + 1
            individuo[1] = fitness
    return populacao
