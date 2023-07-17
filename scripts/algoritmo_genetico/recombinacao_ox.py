import numpy as np


def recombinacao_ox(cromossomo_p1, cromossomo_p2):
    """
    Realiza a recombinação OX1 sobre dois cromossomos
    :param np.ndarray cromossomo_p1: cromossomo do pai 1
    :param np.ndarray cromossomo_p2: cromossomo do pai 2
    :return: dois descendentes
    """
    n_alelo = len(cromossomo_p1)
    pais = [cromossomo_p1, cromossomo_p2]
    descendentes = []
    for indice_pai in range(0, 2):
        cromossomo_descendente = np.full(shape=n_alelo, fill_value=-1)
        pos_corte_1 = np.random.randint(low=0, high=n_alelo-1)
        pos_corte_2 = np.random.randint(low=pos_corte_1+1, high=n_alelo)
        secao_cromossomo = pais[indice_pai][pos_corte_1:pos_corte_2]
        cromossomo_descendente[pos_corte_1:pos_corte_2] = secao_cromossomo
        locus = 0
        locus_pai = 0
        while locus < n_alelo:
            if (locus < pos_corte_1) or (locus >= pos_corte_2):
                while pais[indice_pai-1][locus_pai] in cromossomo_descendente:
                    locus_pai += 1
                cromossomo_descendente[locus] = pais[indice_pai-1][locus_pai]
                locus += 1
                locus_pai += 1
            else:
                locus += 1
        descendentes.append([cromossomo_descendente, 0, 0])
    return descendentes
