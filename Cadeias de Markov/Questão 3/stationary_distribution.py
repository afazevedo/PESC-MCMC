""" 
3. Determine numericamente a distribuição estacionária para cada valor de $p$, e indique o estado de menor probabilidade.
"""

import numpy as np
from scipy import linalg as LA

def stationary_distribution(p):
    A = [[(1-p)-1,(1-p),(1-p),(1-p),(1-p),(1-p),(1-p),(1-p),(1-p),(1-p)], 
        [p, -1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, p, -1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, p, -1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, p, -1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, p, -1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, p, -1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, p, -1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, p, -1, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    b = [0,0,0,0,0,0,0,0,0,1]
    
    stationary = np.linalg.solve(A, b) # Resolvendo o sistema linear
    
    stationary_sorted = sorted(stationary) # Ordenar de forma crescente
    min_pi = stationary_sorted[0] # Pegar o menor elemento
    return stationary, min_pi 