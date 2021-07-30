from read_files import *
from initial_solution import *
import networkx as nx
import numpy as np 
import math
import random
import matplotlib.pyplot as plt
import time
import os

def weight(c, G):
        '''
        Calculate weight
        '''
        total_cost = 0
        for i,j in G.edges():
            total_cost += c[i,j]

        return total_cost

def rejection():
    path = 'D:\\mndzvd\\Documentos\\GitHub\\project_mcmc\\instances\\states_brazil.txt'
    n, m, matrix_cost = readFiles(path, True)
    G = create_graph(n, matrix_cost)
    while True:
        T = generate_random_tree(G)
        if weight(matrix_cost, T) <= 13000:
            return T
            break 

start_time = time.time()

T = rejection()
best_solution = nx.diameter(T)
for i in range(50):
    T = rejection()
    if nx.diameter(T) < best_solution:
        best_solution = nx.diameter(T)

print('=====================================')
print("Melhor diâmetro: ", best_solution)
print("--- %s seconds ---" % (time.time() - start_time))
print('=====================================')

