import numpy as np


def fitness_sharing(populacao: np.ndarray, sigma: float, alpha: float):
    """
    Atualiza a medida de fitness sharing da população
    :param populacao: população cara calcular o fitness sharing
    :param sigma: limiar de similaridade da função do fitness sharing
    :param alpha: forma da função de fitness sharing
    :return: população com a métrica de fitness sharing atualizada
    """
    for individuo in populacao:
        if individuo[2] == 0:
            similaridade = []
            i = 0
            while i < len(populacao):
                distancia = calc_distancia(individuo[0], populacao[i][0])
                if distancia < sigma:
                    similaridade.append(1 - (distancia/sigma)**alpha)
                else:
                    similaridade.append(0)
                i += 1
            fit_sharing = individuo[1]/sum(similaridade)
            individuo[2] = fit_sharing
    return populacao


def calc_distancia(individuo_i: np.ndarray, individuo_j: np.ndarray):
    """
    Calcula a distância entre o indivíduo i e o indivíduo j
    :param individuo_i: Primeiro indivíduo para o cálculo da distância
    :param individuo_j: Segundo indivíduo para o cálculo da distância
    :return: Distância entre os indivíduos
    """
    distancia = np.sqrt((individuo_i[0] - individuo_j[0])**2 + (individuo_i[1] - individuo_j[1])**2)
    return distancia
