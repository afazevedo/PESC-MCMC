"""
1. Construa a cadeia de Markov deste processo mostrando a matriz de transição de probabilidade em função de $p$.
"""
import numpy as np

def read_matrix(p):
    T = np.zeros((10,10))

    for i in range(10):
        for j in range(10):
            T[j, 0] = 1-p
        if i < 9:
            T[i, i+1] = p
        if i == 9:
            T[i,i] = p
    return T