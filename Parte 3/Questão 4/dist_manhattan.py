"""
3. Seja $d(t)$ o valor esperado da distância (de Manhattan) entre $X_t$ (o espaço no tempo $t$) e a origem. Utilize o simulador para estimar $d(t)$ para $t \in \{10, 100, 1000\}$, para cada valor de $p$. O que você pode concluir?

"""

from simulador import *

# Distância do taxi
def taxi_metric(x):
    return abs(1-x[0]) + abs(1-x[1]) 


def simula_taxi(t, p):
    caminho = [(1,1)]
    pi_0 = simulador_latice((1,1), p)  
    caminho.append(pi_0)
    for i in range(t):
        neighbor = simulador_latice(pi_0, p)   
        caminho.append(neighbor)
        pi_0 = neighbor
    x_t = caminho[len(caminho)-1]
    dist = taxi_metric(x_t)
    return dist

def monte_carlo_taxi(t,p,n):
    soma = 0
    for i in range(n):
        dist = simula_taxi(t, p)
        soma = soma + dist
    return(soma/n)

