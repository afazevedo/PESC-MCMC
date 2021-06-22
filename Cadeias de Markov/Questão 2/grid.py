import numpy as np
import matplotlib.pyplot as plt

"""
    Passeio aleatório:
    distribuição estacionária é dado pelo grau do vértice i dividido por 2 vezes o número de arestas.

"""

n = 100 # número de vértices
pi_grid = np.zeros(100) # n = 100

for i in range(100):
    if i == 0 or i == 9 or i == 90 or i == 99: #quinas
        pi_grid[i] = 2/360
    elif 1 <= i <= 8: #borda topo
        pi_grid[i] = 3/360
    elif 91 <= i <= 98: #borda fundo
        pi_grid[i] = 3.0/360
    elif i % 10 == 0 and i != 0 and i != 90: #borda esquerda
        pi_grid[i] = 3/360
    elif i % 10 == 9 and i != 9 and i != 99: #borda direita
        pi_grid[i] = 3/360
    else: #interior
        pi_grid[i] = 4/360 

T_grid = np.zeros((100,100))

for i in range(100):
    T_grid[i][i] = 0.5

    if i == 0: # Quinas
        T_grid[i][i+1] = 0.25
        T_grid[i][i+10] = 0.25
        T_grid[i+9][i+8] = 0.25
        T_grid[i+9][i+19] = 0.25
    elif i == 99:
        T_grid[i][i-1] = 0.25
        T_grid[i][i-10] = 0.25
        T_grid[i-9][i-8] = 0.25
        T_grid[i-9][i-19] = 0.25
    elif 1 <= i <= 8: #borda topo
        T_grid[i][i-1] = 1/6
        T_grid[i][i+1] = 1/6
        T_grid[i][i+10] = 1/6
    elif 91 <= i <= 98: #borda fundo
        T_grid[i][i-1] = 1/6
        T_grid[i][i+1] = 1/6
        T_grid[i][i-10] = 1/6
    elif i != 90 and i != 0 and i % 10 == 0: #borda esquerda
        T_grid[i][i-10] = 1/6
        T_grid[i][i+10] = 1/6
        T_grid[i][i+1] = 1/6
    elif i % 10 == 9 and i != 9 and i != 99: #borda direita
        T_grid[i][i-10] = 1/6
        T_grid[i][i+10] = 1/6
        T_grid[i][i-1] = 1/6
    else:
        if i != 90 and i != 9: #interior
            T_grid[i][i+1] = 1/8
            T_grid[i][i-1] = 1/8
            T_grid[i][i+10] = 1/8
            T_grid[i][i-10] = 1/8

N = 1000

# A = np.matmul(pi_grid, T_grid)
# pi_grid = np.around(pi_grid, 7)
# A = np.around(A, 7)
# print(A == pi_grid)

pi_t = np.zeros(n) #distribuição t
pi_t[0] = 1 # origem

# Variação da distância total

var_total_grid = []
var_total = 0
for j in range(n):
    var_total = var_total + (abs(pi_t[j] - pi_grid[j]))
var_total_grid.append(var_total/2)


for i in range(1, N+1):
    pi_t = np.matmul(pi_t, T_grid)

    var_total = 0
    for j in range(n):
        var_total = var_total + (abs(pi_t[j] - pi_grid[j]))
    var_total_grid.append(var_total/2)