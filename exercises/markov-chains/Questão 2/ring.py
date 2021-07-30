import numpy as np
import matplotlib.pyplot as plt

"""
Note que: A distribuição estacionária não precisa levar em conta o self-loop, pois intuitivamente é constante em todo vértice e não fará diferença na convergência. 
"""

""" 
    Passeio aleatório:
    distribuição estacionária é dado pelo grau do vértice i dividido por 2 vezes o número de arestas.
    O anel possui n arestas. E cada nó possue exatamente 2 vértices, logo, a distribuição estacionária será uniforme em 1/n.
"""
N = 1000 # Número de amostras

n = 100 # Numero de vertices
pi_ring = np.ones(n)/n # Distribuição estacionária
T_ring = np.zeros((n,n)) #Matriz de transição

for i in range(n):
    T_ring[i][i] = 0.5  #lazy

    if i != n-1:
        T_ring[i][i+1] = 0.25 
    else:
        T_ring[i][0] = 0.25

    T_ring[i][i-1] = 0.25


pi_t = np.zeros(n) #distribuição t
pi_t[0] = 1 # origem

# Variação da distância total

var_total_ring = []
var_total = 0
for j in range(n):
    var_total = var_total + (abs(pi_t[j] - pi_ring[j]))
var_total_ring.append(var_total/2)

for i in range(1, N+1):
    pi_t = np.matmul(pi_t, T_ring)

    var_total = 0
    for j in range(n):
        var_total = var_total + (abs(pi_t[j] - pi_ring[j]))
    var_total_ring.append(var_total/2)