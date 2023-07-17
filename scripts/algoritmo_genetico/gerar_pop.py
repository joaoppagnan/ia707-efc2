import numpy as np


def gerar_pop(n_populacao, n_alelos):
    """
    Gera a população inicial com base em uma permutação aleatória
    :param n_populacao: tamanho da população inicial
    :param n_alelos: quantidade de alelos
    :return: população inicial num array do numpy
    """
    populacao = []
    for i in range(0, n_populacao):
        individuo = []
        for j in range(0, n_alelos):
            gene = np.random.randint(low=1, high=n_alelos + 1)
            while gene in individuo:
                gene = np.random.randint(low=1, high=n_alelos + 1)
            individuo.append(gene)
        populacao.append([np.array(individuo), 0, 0])  # a segunda dimensão armazena o fitness e a terceira o custo
    return np.array(populacao, dtype=object)
