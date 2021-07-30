
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


def local_search(spanTree, C, B):
    n = nx.Graph.number_of_nodes(spanTree)

    viavel = False
    L = n//2
    labelNodes = np.zeros(n)


    spanCost = weight(C, spanTree)
    # print("Custo antes:", spanCost)

    while True:
        improve = False

        for k in range(L):
            node_center = nx.algorithms.distance_measures.center(spanTree)
            if len(node_center) < 2:
                minPathleft, path = nx.single_source_bellman_ford(spanTree, node_center[0])
                for node in range(n):
                    labelNodes[node] = minPathleft[node] 
            else:
                minPathleft, path = nx.single_source_bellman_ford(spanTree, node_center[0])
                minPathRight, path = nx.single_source_bellman_ford(spanTree,node_center[1])
                
                for node in range(n):
                    if minPathleft[node] < minPathRight[node]:
                        labelNodes[node] = minPathleft[node]
                    else:
                        labelNodes[node] = minPathRight[node]
            lcr = []
            for i in range(n):
                if labelNodes[i] == k:
                    lcr.append(i)

            if len(lcr) > 0:
                chegada = np.zeros(n, dtype=bool)
                for i in lcr:
                    greatBenefit = 10000 
                    greatInd = -1 
                    node_chose = -1
                    
                    neighbors = nx.all_neighbors(spanTree, i)
                    for j in neighbors:
                        if labelNodes[j] <= labelNodes[i]:
                            node_chose = j 
                        
                    for j in range(n):
                        if node_chose != -1 and i != j and node_chose != j and C[node_chose, i] > C[i,j] and (C[i,j] - C[node_chose, i]) < greatBenefit and not nx.Graph.has_edge(spanTree, i,j) and not chegada[i]:
                            greatBenefit = C[i,j] - C[node_chose, i]
                            greatInd = j 
                            
                    if greatInd != -1:
                        aux_tree = nx.Graph.copy(spanTree)
                        aux_cost = weight(C, spanTree)
                        
                        spanCost = spanCost + (C[i,greatInd] - C[node_chose, i])
                        nx.Graph.add_edge(spanTree, i, greatInd)
                        nx.Graph.remove_edge(spanTree, node_chose, i)
                        
                        if not nx.has_path(spanTree, node_chose, greatInd):
                            spanTree = aux_tree
                            spanCost = aux_cost
                        else:
                            chegada[greatInd] = 1
                            labelNodes[i] = labelNodes[greatInd] + 1
                            if spanCost + (C[i,greatInd] - C[node_chose, i]) <= spanCost:
                                improve = True
                            
                        if spanCost <= B:
                            viavel = True 
                            print("Custo depois: ", spanCost)
                            diametro = nx.diameter(spanTree) 
                            nx.draw(spanTree, with_labels=True)
                            plt.show()    
                    
        if viavel or not improve:
            break

