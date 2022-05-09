import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Analise:

    def __init__ (self):

        dialog1 = int(input("Olá, bem-vindo ao script sobre vendas de jogos. \n O que deseja saber? \n 1 - Vendas globais por plataforma \n"))
        
        if(dialog1 == 1):

            self.VendasPorPlataforma()

        else:

            dialog2 = int(input("Opção Inválida. Deseja tentar novamente? \n 1 - Sim \n 2 - Não \n"))

            if(dialog2 == 1):

                self.__init__()

            else:

                print("Volte sempre!")

    def VendasPorPlataforma (self):

        dadosCSV = pd.read_csv("./vgsales.csv")
        dadosCSV = dadosCSV.dropna()

        x = dadosCSV['Platform']
        y = dadosCSV['Global_Sales']
        
        graficoBar = plt.bar(x, y, color="royalblue")
        plt.title('Vendas por plataforma')
        plt.xlabel('Plataforma')
        plt.ylabel('Vendas')
        plt.xticks(rotation=45)
        plt.show()
        plt.savefig('grafico_vendas.png')

Analise() #Executar aplicação