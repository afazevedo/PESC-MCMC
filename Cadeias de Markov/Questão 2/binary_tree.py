import numpy as np
import matplotlib.pyplot as plt

"""
    Passeio aleatório:
    distribuição estacionária é dado pelo grau do vértice i dividido por 2 vezes o número de arestas.
    Uma árvore (binária ou não) possui n-1 arestas. Neste caso, vamos direcionar ele, nos dando 2*(n-1) arestas. 
    Dividiremos esse caso em 3 casos:
    
    1- Raiz possui dois filhos (grau 2)
    2- O tronco da árvore possui 3 ligações, 2 filhos e uma aresta pro pai (grau 3)
    3- O número de folhas é (n-1)/2, e elas só possuem ligação com o pai. (grau 1)
    
    Por definição, uma árvore binária cheia não pode ter tamanho par devido a raiz. Logo, pegaremos o número mais próximo múltiplo de 2, 2*64 + 1 => n=127. 
    A distribuição de probabilidade será uniforme para o que sobrar do lazy.
"""

n = 127 # número de vértices
pi_tree = np.array([2/252] + [3/252]*62 + [1/252]*64) # Estacionária. Raiz + tronco (62 vértices) + folhas (64 vértices)
T_tree = np.zeros((n,n)) #matriz de transição

for i in range(n):
    T_tree[i][i] = 0.5 #lazy

    if i == 0: # raiz
        T_tree[i][i+1] = 0.25 # Filho 1
        T_tree[i][i+2] = 0.25 # Filho 2

    elif 0 < i < 63: # tronco
        T_tree[i][2*i + 1] = 1/6 # Filho 1
        T_tree[i][2*i + 2] = 1/6 # Filho 2
        T_tree[i][int((i-1)/2)] = 1/6 # Pai

    else: # folhas 
        T_tree[i][int((i-1)/2)] = 0.5 # Pai


N = 1000
pi_t = np.zeros(n) #distribuição t
pi_t[0] = 1 # origem

# Variação da distância total

var_total_tree = []

var_total = 0
for j in range(n):
    var_total = var_total + (abs(pi_t[j] - pi_tree[j]))
var_total_tree.append(var_total/2)
    
for i in range(1, N):
    pi_t = np.matmul(pi_t, T_tree)

    var_total = 0
    for j in range(n):
        var_total = var_total + (abs(pi_t[j] - pi_tree[j]))
    var_total_tree.append(var_total/2)