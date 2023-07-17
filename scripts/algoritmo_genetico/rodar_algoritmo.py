import numpy as np
from algoritmo_genetico import algoritmo_genetico


N_POPULACAO = 1000
CRITERIO_DE_PARADA = 20
Q_TORNEIO = 10
P_MUTACAO = 0.5
PATH_MAT_DADOS = '../../dados/elshafei_QAP.mat'
REALIZACOES = 10
PATH_SALVAR_MELHORES_SOLUCOES = "../../melhores_solucoes/algoritmo-genetico/"
PATH_GRAFICOS = "../../graficos/algoritmo-genetico/"

solucoes = []
fitnesses = []
custos = []

for realizacao in range(0, REALIZACOES):
    solucao, fitness, custo = algoritmo_genetico(n_populacao=N_POPULACAO, q_torneio=Q_TORNEIO,
                                                 criterio_de_parada=CRITERIO_DE_PARADA,
                                                 p_mutacao=P_MUTACAO, path_mat_dados=PATH_MAT_DADOS,
                                                 realizacao=realizacao, path_graficos=PATH_GRAFICOS)
    solucoes.append(solucao)
    fitnesses.append(fitness)
    custos.append(custo)

np.savetxt(fname=PATH_SALVAR_MELHORES_SOLUCOES+'solucoes.txt', X=np.array(solucoes).reshape((len(solucoes), 19)),
           delimiter=',', newline='\n', fmt='%i')
np.savetxt(fname=PATH_SALVAR_MELHORES_SOLUCOES+'fitnesses.txt', X=np.array(fitnesses).reshape((len(fitnesses), 1)),
           delimiter=',', newline='\n', fmt='%.4f')
np.savetxt(fname=PATH_SALVAR_MELHORES_SOLUCOES+'custos.txt', X=np.array(custos).reshape((len(custos), 1)),
           delimiter=',', newline='\n', fmt='%i')
np.savetxt(fname=PATH_SALVAR_MELHORES_SOLUCOES+'custos-valor-medio.txt', X=np.array([np.mean(custos)]),
           delimiter=',', newline='\n', fmt='%i')
np.savetxt(fname=PATH_SALVAR_MELHORES_SOLUCOES+'custos-desvio-padrao.txt', X=np.array([np.std(custos)]),
           delimiter=',', newline='\n')
