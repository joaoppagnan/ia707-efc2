import numpy as np
import scipy.io
from gerar_pop import gerar_pop
from calc_fitness import calc_fitness
from selecao_torneio import selecao_torneio
from recombinacao_crossover_aritmetico import recombinacao_crossover_aritmetico
from mutacao_uniforme import mutacao_uniforme
from fitness_sharing import fitness_sharing
from gerar_grafico import gerar_grafico_fitness, gerar_grafico_curvas


def algoritmo_genetico(n_populacao: int, q_torneio: float, criterio_de_parada: int, p_mutacao: float,
                       limite_inferior: float, limite_superior: float, sigma: float, alpha: float,
                       realizacao: int, path_graficos: str):
    """
    Funcao principal do algoritmo genetico
    :param n_populacao: número de indivíduos na população
    :param q_torneio: fração da população presente no torneio
    :param criterio_de_parada: critério de parada a ser utilizado
    :param p_mutacao: probabilidade de acontecer uma mutação
    :param limite_inferior: limite inferior da região de busca
    :param limite_superior: limite superior da região de busca
    :param sigma: limiar de similaridade do fitness sharing
    :param alpha: forma da similaridade do fitness sharing
    :param str realizacao: realização do algoritmo
    :param str path_graficos: caminho para salvar os gráficos
    :return: melhor individuo e melhor fitness
    """

    # gerar população inicial
    populacao = gerar_pop(n_populacao)

    # calcula o fitness para ela
    populacao = calc_fitness(populacao)

    # calcula o fitness sharing para ela
    populacao = fitness_sharing(populacao, sigma, alpha)

    # inicializa o array para armazenar o fitness médio e o melhor fitness
    dados_fitness = np.empty((criterio_de_parada, 2))

    # calcula para a população inicial
    dados_fitness[0, 0] = np.mean(populacao[:, 1])  # fitness sharing
    dados_fitness[0, 1] = np.max(populacao[:, 1])  # melhor fitness

    # entra no loop principal do algoritmo
    for n_geracao in range(1, criterio_de_parada):

        # agora vai realizar a seleção -> recombinação -> mutação até que a população aumente para 3N/2 individuos
        while len(populacao) < 2*n_populacao:
            # seleciona dois pais
            pais = []
            for i in range(0, 2):
                pai = selecao_torneio(populacao=populacao, n_populacao=n_populacao, q_torneio=q_torneio)
                pais.append(pai)

            # checa se são indivíduos diferentes e, caso forem iguais, realiza uma nova seleção
            while np.array_equal(pais[0][0], pais[1][0]):
                pai = selecao_torneio(populacao=populacao, n_populacao=n_populacao, q_torneio=q_torneio)
                pais[1] = pai

            # realiza a recombinação para produzir um descendente
            descendentes = recombinacao_crossover_aritmetico(cromossomo_p1=pais[0][0], cromossomo_p2=pais[1][0])

            # realiza a mutação com uma chance dada por pm
            for descendente in descendentes:
                descendente[0] = mutacao_uniforme(cromossomo=descendente[0], p_mutacao=p_mutacao,
                                                  a=limite_inferior, b=limite_superior)

            # adiciona os descendentes na população
            populacao = np.vstack((populacao, np.array(descendentes, dtype=object)))

            # atualiza os fitness
            populacao = calc_fitness(populacao)

            # atualiza o fitness sharing
            populacao = fitness_sharing(populacao, sigma, alpha)

        # elimina os N individuos de menor fitness sharing
        populacao = populacao[populacao[:, 2].argsort()][n_populacao:len(populacao)]

        # atualiza o array
        dados_fitness[n_geracao, 0] = np.mean(populacao[:, 1])  # fitness medio
        dados_fitness[n_geracao, 1] = np.max(populacao[:, 1])  # melhor fitness

    # gera o grafico do fitness
    titulo = r"Curvas de $fitness$ médio e máximo para a realização " + str(realizacao+1) +\
             "\n do algoritmo genético com $fitness$ $sharing$"
    nome_do_arquivo = "fitness-realizacao-" + str(realizacao+1) + ".pdf"
    legenda = [r"$Fitness$ médio", r"$Fitness$ máximo"]
    gerar_grafico_fitness(dados=dados_fitness, titulo=titulo, eixo_x="Geração", eixo_y=r"\it{Fitness}",
                          nome_do_arquivo=path_graficos+nome_do_arquivo, legenda=legenda)

    # gera o grafico das curvas de nível
    titulo = r"Distribuição da população final sobre as curvas de nível de $f(x, y)$" +\
             "\n para a realização " + str(realizacao+1) + " do algoritmo genético com $fitness$ $sharing$"
    nome_do_arquivo = "distribuicao-realizacao-" + str(realizacao+1) + ".pdf"
    legenda = ["Curvas de nível", "População"]
    gerar_grafico_curvas(dados=populacao, titulo=titulo, eixo_x="$x$", eixo_y="$y$", legenda=legenda,
                         nome_do_arquivo=path_graficos+nome_do_arquivo)

    return populacao[-1]
