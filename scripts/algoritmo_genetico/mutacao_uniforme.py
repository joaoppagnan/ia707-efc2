import numpy as np


def mutacao_uniforme(cromossomo: np.ndarray, p_mutacao: float, a: float, b: float):
    """
    Realiza uma mutação uniforme no cromossomo
    :param cromossomo: cromossomo que será mutado
    :param p_mutacao: probabilidade de haver mutação
    :param a: limite inferior da região
    :param b: limite superior da região
    :return: cromossomo mutado
    """
    if np.random.rand() <= p_mutacao:
        cromossomo_mutado = []
        for i in range(0, 2):
            M = np.random.uniform(low=a, high=b)
            cromossomo_mutado.append(cromossomo[i] + M)
            if cromossomo_mutado[i] < a:
                cromossomo_mutado[i] = a
            elif cromossomo_mutado[i] > b:
                cromossomo_mutado[i] = b
        return np.array(cromossomo_mutado)
    else:
        return cromossomo
