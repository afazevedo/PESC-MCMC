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
                                Questão 2
#----------------------------------------------------------------------------------------------------------#
    Considere um passeio aleatório preguiçoso (com $p=\frac{1}{2}$) caminhando sobre um grafo com $n=100$ 
    vértices. Estamos interessados em entender a convergência da distribuição $\pi(t)$ em diferentes grafos. 
    Assuma que o passeio sempre inicia sua caminhada no vértice $1$, ou seja, $\pi_1(0) = 1$. 
    Considere os seguintes grafos: grafos em anel, árvore binária cheia, grafo em reticulado com 
    duas dimensões (grid 2D).
#----------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------#
"""



import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

from ring import *
from binary_tree import *
from grid import *

"""
    Tabela
"""

print(tabulate([[T_ring]], headers=["Matriz de Transição: Grafo Anel"]))
print(tabulate([[T_tree]], headers=["Matriz de Transição: Grafo Árvore Binária"]))
print(tabulate([[T_grid]], headers=["Matriz de Transição: Grafo Grid"]))

print(tabulate([[pi_ring]], headers=["Distribuição Estacionária: Grafo Anel"]))
print(tabulate([[T_tree]], headers=["Distribuição Estacionária: Grafo Árvore Binária"]))
print(tabulate([[T_grid]], headers=["Distribuição Estacionária: Grafo Grid"]))

""" 
    Gráfico
"""

# plt.plot(var_total_ring, c ='blue')
# plt.plot(var_total_tree, c = 'red')
# plt.plot(var_total_grid, c = 'green')
# plt.xscale('log')
# plt.yscale('log')
# plt.legend(["Grafo Anel", "Árvore Binária Cheia", "Grid 2D"])
# plt.show()
