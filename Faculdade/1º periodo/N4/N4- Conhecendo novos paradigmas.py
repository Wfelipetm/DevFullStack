import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


class Pessoa:
    def __init__(self, nome, ender):
        self.set_nome(nome)
        self.set_ender(ender)

    def set_nome(self, nome):
        self.nome = nome

    def set_ender(self, ender):
        self.ender = ender

    def get_nome(self):
        return self.nome

    def get_ender(self):
        return self.ender

    def imprimir_dados(self):
        print(f'Nome: {self.get_nome()}, Endereço: {self.get_ender()}')


class Grafico:
    def __init__(self, lista_despesas):
        self.lista_despesas = lista_despesas
        self.imprimir_graficos()

    def padrao_do_grafico(self):
        plt.xlabel('Dia')
        plt.ylabel('Valores ($)')
        plt.title('Gráficos de Despesas')

    def imprimir_graficos(self):
        self.padrao_do_grafico()
        for despesa in self.lista_despesas:
            mLista = despesa.dicionario.items()
            cor = despesa.cor
            nome = despesa.nome
            x, y = zip(*mLista)
            plt.plot(x, y, label=nome, marker='o',
                     markerfacecolor='blue',
                     markersize=12,
                     color=cor,
                     linewidth=4)
        plt.legend()
        plt.show()

    def regressao_linear(self, id_grafico):
        despesa = self.lista_despesas[id_grafico]
        mLista = despesa.dicionario.items()
        cor = despesa.cor
        nome = despesa.nome
        dias, valores = zip(*mLista)
        dias = np.array(dias)
        valores = np.array(valores)
        dias = dias.reshape(-1, 1)
        valores = valores.reshape(-1, 1)
        regr = LinearRegression()
        regr.fit(X=dias, y=valores)
        plt.plot(dias, regr.predict(dias),
                 color='blue',
                 label="Regressão Linear")

        x, y = zip(*mLista)
        plt.plot(x, y, label=nome+str(" - original"),
                 marker='o',
                 markerfacecolor='olive',
                 markersize=12,
                 color=cor,
                 linewidth=4)

        plt.legend()
        plt.show()


class Despesa:
    def __init__(self, dicionario, cor, nome):
        self.dicionario = dicionario
        self.cor = cor
        self.nome = nome


maio = Despesa({1: 100, 5: 800, 17: 230, 20: 88, 29: 280}, 'skyblue', 'maio')
junho = Despesa({1: 60, 5: 769, 19: 311, 29: 280}, 'red', 'junho')
julho = Despesa({1: 150, 5: 900, 16: 138, 20: 188, 30: 60}, 'olive', 'julho')
lista_despesas = [maio, junho, julho]

grafico = Grafico(lista_despesas)

id_mes = 2
grafico.regressao_linear(id_mes)
