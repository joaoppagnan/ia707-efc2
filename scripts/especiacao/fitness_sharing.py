import numpy as np
from calc_distancia import calc_distancia

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
