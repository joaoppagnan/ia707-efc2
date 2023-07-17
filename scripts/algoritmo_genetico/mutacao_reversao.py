import numpy as np


def mutacao_reversao(cromossomo: np.ndarray, p_mutacao: float):
    """
    Realiza uma mutação de reversão na permutação
    :param cromossomo: cromossomo que será mutado
    :param p_mutacao: probabilidade de haver mutação
    :return: cromossomo mutado
    """
    if np.random.rand() <= p_mutacao:
        n_alelos = len(cromossomo)
        cromossomo_mutado = np.full(shape=n_alelos, fill_value=-1)
        indice_1 = np.random.randint(low=0, high=n_alelos-1)
        indice_2 = np.random.randint(low=indice_1+1, high=n_alelos)
        i = 0
        j = 0
        while i < n_alelos:
            if (i >= indice_1) & (i <= indice_2):
                cromossomo_mutado[i] = cromossomo[indice_2 - j]
                j += 1
            else:
                cromossomo_mutado[i] = cromossomo[i]
            i += 1
        return cromossomo_mutado
    else:
        return cromossomo
