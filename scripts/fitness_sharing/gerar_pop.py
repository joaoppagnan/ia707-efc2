import numpy as np


def gerar_pop(n_populacao):
    """
    Gera a população inicial com base em um vetor aleatório com dois elementos
    :param n_populacao: tamanho da população inicial
    :return: população inicial num array do numpy
    """
    populacao = []
    for i in range(0, n_populacao):
        individuo = []
        for j in range(0, 2):
            gene = np.random.uniform(low=-1, high=2)
            individuo.append(gene)
        populacao.append([np.array(individuo), 0, 0])  # a segunda dimensão armazena o fitness e a terceira o fitness
                                                       # sharing
    return np.array(populacao, dtype=object)
