import numpy as np
import scipy.io
from gerar_pop import gerar_pop
from calc_fitness import calc_fitness_qap
from selecao_torneio import selecao_torneio
from recombinacao_crossover_aritmetico import recombinacao_ox
from mutacao_reversao import mutacao_reversao
from gerar_grafico import gerar_grafico


def algoritmo_genetico(n_populacao: int, q_torneio: float, criterio_de_parada: int, p_mutacao: float,
                       path_mat_dados: str, realizacao: int, path_graficos: str):
    """
    Funcao principal do algoritmo genetico
    :param n_populacao: número de indivíduos na população
    :param q_torneio: fração da população presente no torneio
    :param criterio_de_parada: critério de parada a ser utilizado
    :param p_mutacao: probabilidade de acontecer uma mutação
    :param str path_mat_dados: caminho para a matriz com os dados
    :param str realizacao: realização do algoritmo
    :param str path_graficos: caminho para salvar os gráficos
    :return: melhor individuo e melhor fitness
    """

    # carrega os dados
    mat_dados = scipy.io.loadmat(path_mat_dados)
    distancias = mat_dados['D']
    fluxos = mat_dados['W']

    # vê quantos alelos serão necessários
    n_alelos = fluxos.shape[0]

    # gerar população inicial
    populacao = gerar_pop(n_populacao, n_alelos)

    # calcula o fitness para ela
    populacao = calc_fitness_qap(populacao, distancias, fluxos)

    # inicializa o array para armazenar o custo médio, o fitness médio e o melhor custo
    dados_custo_fitness = np.empty((criterio_de_parada, 3))

    # calcula para a população inicial
    dados_custo_fitness[0, 0] = np.mean(populacao[:, 1])  # fitness medio
    dados_custo_fitness[0, 1] = np.mean(populacao[:, 2])  # custo medio
    dados_custo_fitness[0, 2] = np.min(populacao[:, 2])  # melhor custo

    # entra no loop principal do algoritmo
    for n_geracao in range(1, criterio_de_parada):

        # agora vai realizar a seleção -> recombinação -> mutação até que a população aumente para 3N/2 individuos
        while len(populacao) < 2*n_populacao:
            # seleciona dois pais
            pais = []
            for i in range(0, 2):
                pai = selecao_torneio(populacao=populacao, n_populacao=n_populacao, q_torneio=q_torneio)
                pais.append(pai)

            # realiza a recombinação para produzir um descendente
            descendentes = recombinacao_ox(cromossomo_p1=pais[0][0], cromossomo_p2=pais[1][0])

            # realiza a mutação com uma chance dada por pm
            for descendente in descendentes:
                descendente[0] = mutacao_reversao(cromossomo=descendente[0], p_mutacao=p_mutacao)

            # adiciona os descendentes na população
            populacao = np.append(populacao, descendentes, axis=0)

            # atualiza os fitness
            populacao = calc_fitness_qap(populacao, distancias, fluxos)

            # atualiza o array
            dados_custo_fitness[n_geracao, 0] = np.mean(populacao[:, 1])  # fitness medio
            dados_custo_fitness[n_geracao, 1] = np.mean(populacao[:, 2])  # custo medio
            dados_custo_fitness[n_geracao, 2] = np.min(populacao[:, 2])  # melhor custo

        # elimina os N individuos de menor fitness
        populacao = populacao[populacao[:, 1].argsort()][n_populacao:len(populacao)]

    # gera o grafico
    titulo = "Curvas de custo médio e mínimo para a realização " + str(realizacao+1) + " do algoritmo genético"
    nome_do_arquivo = "realizacao-" + str(realizacao+1) + ".pdf"
    legenda = ["Custo médio", "Custo mínimo"]
    gerar_grafico(dados=dados_custo_fitness, titulo=titulo, eixo_x="Geração", eixo_y="Custo",
                  nome_do_arquivo=path_graficos+nome_do_arquivo, legenda=legenda)

    return populacao[-1]
