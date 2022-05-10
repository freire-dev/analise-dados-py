import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Analise:

    def __init__ (self):

        dialog1 = int(input("Olá, bem-vindo ao script sobre vendas de jogos. \n\n O que deseja saber? \n\n 1 - Total ($) em vendas globais por plataforma \n 2 - Média ($) em vendas globais por plataforma \n 3 - Total ($) em vendas globais por gênero de jogos \n 4 - Média ($) em vendas globais por gênero de jogos \n\n"))
        
        if(dialog1 == 1):

            self.totalVendasPorPlataforma()

        elif(dialog1 == 2):

            self.mediaVendasPorPlataforma()

        elif(dialog1 == 3):

            self.totalVendasGenero()

        elif(dialog1 == 4):

            self.mediaVendasGenero()

        else:

            dialog2 = int(input("Opção Inválida. Deseja tentar novamente? \n 1 - Sim \n 2 - Não \n"))

            if(dialog2 == 1):

                self.__init__()

            else:

                print("Volte sempre!")

    def totalVendasPorPlataforma (self):

        dadosCSV = pd.read_csv("./vgsales.csv")
        dadosCSV = dadosCSV.dropna()

        dadosVendas = dadosCSV[['Platform','Global_Sales']].groupby('Platform').sum()
        dadosVendas.plot(kind='bar', color='royalblue')
        plt.xlabel('Plataforma')
        plt.xticks(rotation=90)
        plt.ylabel('Total em vendas')
        plt.title('Total ($) de vendas por plataforma')
        plt.show()

    def mediaVendasPorPlataforma (self):

        dadosCSV = pd.read_csv("./vgsales.csv")
        dadosCSV = dadosCSV.dropna()

        dadosVendas = dadosCSV[['Platform','Global_Sales']].groupby('Platform').mean()
        dadosVendas.plot(kind='bar', color='red')
        plt.xlabel('Plataforma')
        plt.xticks(rotation=90)
        plt.ylabel('Média ($) em vendas')
        plt.title('Média de vendas por plataforma')
        plt.show()

    def totalVendasGenero (self):

        dadosCSV = pd.read_csv("./vgsales.csv")
        dadosCSV = dadosCSV.dropna()

        dadosVendas = dadosCSV[['Genre','Global_Sales']].groupby('Genre').sum()
        dadosVendas.plot(kind='bar', color='green')
        plt.xlabel('Gênero')
        plt.xticks(rotation=90)
        plt.ylabel('Total ($) em vendas')
        plt.title('Total de vendas por gênero de jogos')
        plt.show()

    def mediaVendasGenero(self):

        dadosCSV = pd.read_csv("./vgsales.csv")
        dadosCSV = dadosCSV.dropna()

        dadosVendas = dadosCSV[['Genre','Global_Sales']].groupby('Genre').mean()
        dadosVendas.plot(kind='bar', color='purple')
        plt.xlabel('Gênero')
        plt.xticks(rotation=90)
        plt.ylabel('Media ($) em vendas')
        plt.title('Média de vendas por gênero de jogos')
        plt.show()


Analise() #Executar aplicação