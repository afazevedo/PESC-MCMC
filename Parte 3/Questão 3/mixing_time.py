""" 
4. Utilizando os dados acima, determine um limitante inferior e superior para o tempo de mistura quando $\epsilon = 10^{-6}$ para cada valor de $p$.
"""
import numpy as np
from scipy import linalg as LA

def mixing_time(delta, eps, min_pi):
    tm_inf = ( (1/delta - 1) * np.log(1/(2*eps)) ) 
    tm_sup = ( (np.log(1/(min_pi*eps)))/delta )
    return tm_inf, tm_sup


