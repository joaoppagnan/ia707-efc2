import numpy as np


def gerar_solucoes(n_solucoes, n_items):
    """
    Gera as soluções da busca aleatoria com base em uma permutação aleatória
    :param n_solucoes: quantidade de soluções
    :param n_items: quantidade de items nas permutações
    :return: conjunto de permutações num array do numpy
    """
    solucoes = []
    for i in range(0, n_solucoes):
        solucao = []
        for j in range(0, n_items):
            elemento = np.random.randint(low=1, high=n_items + 1)
            while elemento in solucao:
                elemento = np.random.randint(low=1, high=n_items + 1)
            solucao.append(elemento)
        solucoes.append([np.array(solucao), 0, 0])  # a segunda dimensão armazena o fitness e a terceira o custo
    return np.array(solucoes, dtype=object)
