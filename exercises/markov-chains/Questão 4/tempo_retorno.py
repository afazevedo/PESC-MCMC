"""
    2. Utilize o simulador para estimar a distribuição estacionária da origem (estado (1,1)), ou seja, $\pi_{1,1}$, para cada valor de $p$. Dica: Utilize os tempos de retorno!
"""

from simulador import *

def tempo_de_retorno(p):
    caminho = [(1,1)] # ponto incial
    
    pi_0 = simulador_latice((1,1), p)  
    caminho.append(pi_0)
    it = 0
    
    if pi_0 == (1,1):
        return 1
    else:
        while True:
            it = it + 1
            neighbor = simulador_latice(pi_0, p)   
            caminho.append(neighbor)
            if caminho[len(caminho)-1] == (1,1): #Simula até voltar para a origem (1,1)
                break
            else:
                pi_0 = neighbor
    return it

# Vai gerar amostras para estimar o tempo de retorno
def monte_carlo(p,n):
    soma = 0
    for i in range(n):
        aux = tempo_de_retorno(p)
        soma = soma + aux 
    return soma/n