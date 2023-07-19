import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# config matplotlib
sns.set_style("ticks")
plt.rcParams['savefig.dpi'] = 200
plt.rcParams["figure.dpi"] = 100
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Palatino"],
})


def gerar_grafico_fitness(dados: np.ndarray, titulo: str, eixo_x: str, eixo_y: str,
                          legenda: list, nome_do_arquivo: str):
    """
    Função para gerar um gráfico do fitness com os dados passados
    :param dados: dados a serem plotados
    :param titulo: título do gráfico
    :param eixo_x: nome do eixo x
    :param eixo_y: nome do eixo y
    :param legenda: legenda dos dados
    :param nome_do_arquivo: nome do arquivo a ser salvo
    """
    fig, ax = plt.subplots(nrows=1, ncols=1, tight_layout=True, figsize=(6, 4))
    dado_x = np.arange(0, len(dados[:, 0]), dtype=int)

    # curvas do fitness médio
    ax.plot(dado_x, dados[:, 0], 'bo-', label=legenda[0])

    # curvas do fitness máximo
    ax.plot(dado_x, dados[:, 1], 'rx-', label=legenda[1])

    # renomeia os eixos
    ax.set_xlabel(xlabel=eixo_x)
    ax.set_ylabel(ylabel=eixo_y)

    # outros ajustes do gráfico
    sns.despine()
    ax.legend()
    ax.grid()
    ax.set_title(titulo)

    # salva o gráfico
    fig.savefig(nome_do_arquivo)


def gerar_grafico_curvas(dados: np.ndarray, titulo: str, eixo_x: str, eixo_y: str,
                         legenda: list, nome_do_arquivo: str):
    """
    Função para gerar um gráfico do fitness com os dados passados
    :param dados: dados a serem plotados
    :param titulo: título do gráfico
    :param eixo_x: nome do eixo x
    :param eixo_y: nome do eixo y
    :param legenda: legenda dos dados
    :param nome_do_arquivo: nome do arquivo a ser salvo
    """
    fig, ax = plt.subplots(nrows=1, ncols=1, tight_layout=True, figsize=(6, 4))

    # gera as curvas de nível da função
    x, y = np.meshgrid(np.linspace(-1, 2, 5000), np.linspace(-1, 2, 1000))
    f = x*np.sin(4*np.pi*x) - y*np.sin(4*np.pi*y + np.pi) + 1
    niveis = np.linspace(f.min(), f.max(), 100)

    # desenha as curvas de nível
    ax.contourf(x, y, f, levels=niveis, cmap='jet')

    # distribui os dados no gráfico
    individuos_x = []
    individuos_y = []
    for individuo in dados:
        individuos_x.append(individuo[0][0])
        individuos_y.append(individuo[0][1])
    ax.scatter(x=individuos_x, y=individuos_y, c='black', marker='.', label="População")

    # renomeia os eixos
    ax.set_xlabel(xlabel=eixo_x)
    ax.set_ylabel(ylabel=eixo_y)

    # outros ajustes do gráfico
    sns.despine()
    ax.legend(loc="lower left")
    ax.set_title(titulo)

    # salva o gráfico
    fig.savefig(nome_do_arquivo)
