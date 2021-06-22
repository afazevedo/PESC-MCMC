# -*- coding: utf-8 -*-
"""
# =============================================================================
Author: Amanda Azevedo
Python Version: 3.9.5
Email: afazevedo29@gmail.com
Course: Algoritmos de Monte Carlo e Cadeias de Markov
Date: 26/05/2020
# =============================================================================
"""

"""
#----------------------------------------------------------------------------------------------------------#
                                Questão 4
#----------------------------------------------------------------------------------------------------------#
    Considere uma cadeia de Markov cujo espaço de estados é um látice de duas dimensões sobre os números 
    naturais, ou seja, $S=\{(i,j) | i \geq 1, j \geq 1\}$. Cada estado pode transicionar para um dos seus 
    vizinhos no látice. Entretanto, se afastar da origem (se movimentar para o norte ou para o leste) 
    tem probabilidade $\frac{p}{2}$, e se aproximar da origem tem probabilidade $\frac{(1-p)}{2}$, 
    onde $p$ é um parâmetro do modelo (nas bordas, utilize self-loops). 
    Assuma que $p \in \{0.25, 0.35, 0.45\}$.
#----------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------#
"""
from simulador import *
from tempo_retorno import *
from dist_manhattan import *
from tabulate import tabulate

""" 
    Tabelas 
""" 

amostra_1 = []
amostra_2 = []
amostra_3 = []
n = 100000

mc_1 = monte_carlo(0.25, n)
mc_2 = monte_carlo(0.35, n)
mc_3 = monte_carlo(0.45, n)
amostra_1.append(mc_1)
amostra_2.append(mc_2)
amostra_3.append(mc_3)    
    
table_stationary = [
    ["0.25", 1/amostra_1[0]],
    ["0.35", 1/amostra_2[0]],
    ["0.45", 1/amostra_3[0]]
]
print(tabulate(table_stationary, headers=["p", "n=100000"], tablefmt="latex_booktabs"))

# for t in [10, 100, 1000]:
#     mc_1 = monte_carlo_taxi(t, 0.25, n)
#     mc_2 = monte_carlo_taxi(t, 0.35, n)
#     mc_3 = monte_carlo_taxi(t, 0.45, n)
#     amostra_1.append(mc_1)
#     amostra_2.append(mc_2)
#     amostra_3.append(mc_3) 
    
# table_taxi = [
#     ["0.25", amostra_1[1], amostra_1[2], amostra_1[3]],
#     ["0.35", amostra_2[1], amostra_2[2], amostra_2[3]],
#     ["0.45", amostra_3[1], amostra_3[2], amostra_3[3]]
# ]    
    
# print(tabulate(table_taxi, headers=["p", "t=10", "t=100", "t=1000"], tablefmt="latex_booktabs"))

# """ 
#     Gráfico 
# """ 

# x_tik = [1, 10, 100, 1000, 10000, 100000]
# fig, (ax1, ax2, ax3) = plt.subplots(3, figsize=(16,9))

# amostra_1 = []
# amostra_2 = []
# amostra_3 = []

# fig.suptitle("Estimativa do tempo de retorno")  
# for i in x_tik:
#     mc_1 = monte_carlo(i, 0.25)
#     mc_2 = monte_carlo(i, 0.35)
#     mc_3 = monte_carlo(i, 0.45)
#     ax1.plot(i, mc_1, 'or')
#     ax2.plot(i, mc_2, 'or')
#     ax3.plot(i, mc_3, 'or')
#     amostra_1.append(mc_1)
#     amostra_2.append(mc_2)
#     amostra_3.append(mc_3)
    
# """ 
#         Configurações do gráfico
# """
    
# ax1.plot(x_tik, amostra_1, '-r') 
# ax2.plot(x_tik, amostra_2, '-r')   
# ax3.plot(x_tik, amostra_3, '-r')
    
# ax1.set_title("p = 0.25")
# ax2.set_title("p = 0.35")
# ax3.set_title("p = 0.45")

# ax1.set_xlabel("Número de amostras")
# ax2.set_xlabel("Número de amostras")
# ax3.set_xlabel("Número de amostras")

# ax1.set_title("p = 0.25")
# ax2.set_title("p = 0.35")
# ax3.set_title("p = 0.45")

# ax1.set_xscale("log")
# ax2.set_xscale("log")
# ax3.set_xscale("log")
# plt.show()