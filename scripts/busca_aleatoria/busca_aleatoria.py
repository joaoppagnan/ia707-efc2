import numpy as np
import scipy.io
from gerar_solucoes import gerar_solucoes
from calc_fitness_qap import calc_fitness_qap
from gerar_grafico import gerar_grafico


def busca_aleatoria(n_solucoes: int, criterio_de_parada: int, path_mat_dados: str, realizacao: int, path_graficos: str):
    """
    Funcao principal da busca aleatória
    :param n_solucoes: número de indivíduos na população
    :param criterio_de_parada: critério de parada a ser utilizado
    :param str path_mat_dados: caminho para a matriz com os dados
    :param str realizacao: realização do algoritmo
    :param str path_graficos: caminho para salvar os gráficos
    :return: melhor solução
    """

    # carrega os dados
    mat_dados = scipy.io.loadmat(path_mat_dados)
    distancias = mat_dados['D']
    fluxos = mat_dados['W']

    # vê quantos items serão necessários
    n_items = fluxos.shape[0]

    # inicializa um array para armazenar as soluções
    solucoes = np.array([])

    # inicializa o array para armazenar o custo médio, o fitness médio e o melhor custo
    dados_custo_fitness = np.empty((criterio_de_parada, 3))

    # entra no loop principal da busca
    for n_iteracao in range(0, criterio_de_parada):

        # gera novas solucoes
        try:
            solucoes = np.append(solucoes, gerar_solucoes(n_solucoes, n_items), axis=0)
        except:
            solucoes = gerar_solucoes(n_solucoes, n_items)

        # calcula o fitness para ela
        solucoes = calc_fitness_qap(solucoes, distancias, fluxos)

        # atualiza o array
        dados_custo_fitness[n_iteracao, 0] = np.mean(solucoes[:, 1])  # fitness medio
        dados_custo_fitness[n_iteracao, 1] = np.mean(solucoes[:, 2])  # custo medio
        dados_custo_fitness[n_iteracao, 2] = np.min(solucoes[:, 2])  # melhor custo

        # atualiza a melhor solucao
        melhor_solucao = solucoes[solucoes[:, 1].argsort()][-1]

    # gera o grafico
    titulo = "Curvas de custo médio e mínimo para a realização " + str(realizacao+1) + " da busca aleatória"
    nome_do_arquivo = "iteracao-" + str(realizacao+1) + ".pdf"
    legenda = ["Custo médio", "Custo mínimo"]
    gerar_grafico(dados=dados_custo_fitness, titulo=titulo, eixo_x="Iteração", eixo_y="Custo",
                  nome_do_arquivo=path_graficos+nome_do_arquivo, legenda=legenda)

    return melhor_solucao[0], melhor_solucao[1], melhor_solucao[2]
