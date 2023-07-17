import numpy as np
from busca_aleatoria import busca_aleatoria


N_SOLUCOES = 1000
CRITERIO_DE_PARADA = 20
PATH_MAT_DADOS = '../../dados/elshafei_QAP.mat'
REALIZACOES = 10
PATH_SALVAR_MELHORES_SOLUCOES = "../../melhores_solucoes/busca-aleatoria/"
PATH_GRAFICOS = "../../graficos/busca-aleatoria/"

solucoes = []
fitnesses = []
custos = []

for realizacao in range(0, REALIZACOES):
    solucao, fitness, custo = busca_aleatoria(n_solucoes=N_SOLUCOES, criterio_de_parada=CRITERIO_DE_PARADA,
                                              path_mat_dados=PATH_MAT_DADOS, realizacao=realizacao,
                                              path_graficos=PATH_GRAFICOS)
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
