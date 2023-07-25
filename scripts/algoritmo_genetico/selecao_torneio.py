import numpy as np


def selecao_torneio(populacao, n_populacao, q_torneio):
    """
    Seleciona dois indivíduos com um torneio envolvendo q_torneio*len(populacao) indivíduos
    :param populacao: população
    :param n_populacao: quantidade de individuos na população
    :param q_torneio: fração da quantidade de indivíduos da população selecionados por torneio
    :return: melhor indivíduo do torneio
    """
    individuos_participantes = []
    for i in range(0, q_torneio):
        indices_individuo_sorteado = np.random.randint(low=0, high=n_populacao)
        individuos_participantes.append(populacao[indices_individuo_sorteado, :])
    melhor_individuo = individuos_participantes[np.array(individuos_participantes)[:, 1].argmax()]
    return melhor_individuo
