import numpy as np
from algoritmo_genetico import algoritmo_genetico


N_POPULACAO = 100
CRITERIO_DE_PARADA = 20
Q_TORNEIO = 5
P_MUTACAO = 0.2
LIMITE_INFERIOR = -1.0
LIMITE_SUPERIOR = 2
REALIZACOES = 5
PATH_SALVAR_MELHORES_SOLUCOES = "../../melhores_solucoes/algoritmo-genetico/"
PATH_GRAFICOS = "../../graficos/algoritmo-genetico/"

solucoes = []
fitnesses = []
custos = []

for realizacao in range(0, REALIZACOES):
    solucao, fitness = algoritmo_genetico(n_populacao=N_POPULACAO, q_torneio=Q_TORNEIO,
                                          criterio_de_parada=CRITERIO_DE_PARADA,
                                          p_mutacao=P_MUTACAO, limite_inferior=LIMITE_INFERIOR,
                                          limite_superior=LIMITE_SUPERIOR, realizacao=realizacao,
                                          path_graficos=PATH_GRAFICOS)
    solucoes.append(solucao)
    fitnesses.append(fitness)

np.savetxt(fname=PATH_SALVAR_MELHORES_SOLUCOES+'solucoes.txt', X=np.array(solucoes).reshape((len(solucoes), 2)),
           delimiter=',', newline='\n', fmt='%.10f')
np.savetxt(fname=PATH_SALVAR_MELHORES_SOLUCOES+'fitnesses.txt', X=np.array(fitnesses).reshape((len(fitnesses), 1)),
           delimiter=',', newline='\n', fmt='%.10f')
np.savetxt(fname=PATH_SALVAR_MELHORES_SOLUCOES+'fitnesses-valor-medio.txt', X=np.array([np.mean(fitnesses)]),
           delimiter=',', newline='\n', fmt='%.10f')
np.savetxt(fname=PATH_SALVAR_MELHORES_SOLUCOES+'fitnesses-desvio-padrao.txt', X=np.array([np.std(fitnesses)]),
           delimiter=',', newline='\n', fmt='%.10f')
