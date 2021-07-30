"""
### Questão 7: Contando domínios na Web

Quantos domínios web existem dentro da UFRJ? Mais precisamente, quantos domínios existem dentro do padrão de nomes http://www.[a-z](k).ufrj.br, onde a-z(k) é qualquer sequência de caracteres de comprimento k ou menor? Construa um algoritmo de Monte Carlo para estimar este número.

1.   Descreva a variável aleatória cujo valor esperado está relacionado com a medida de interesse. Relacione analiticamente o valor esperado com a medida de interesse.

2.   Implemente o método de Monte Carlo para gerar amostras e estimar a medida de interesse. Para determinar o valor de uma amostra, você deve consultar o domínio gerado para determinar se o mesmo existe (utilize uma biblioteca www para isto).

3. Assuma que $k = 4$. Seja $w_n$ o valor do estimador do número de domínios após $n$ amostras. Trace um gráfico de $w_n$ em função de $n$ para $n = 1,\dots, 10^4$ (ou mais, se conseguir). O que você pode dizer sobre a convergência de $w_n$?
"""

import random
import string
import random
import numpy as np
from matplotlib import pyplot as plt 
import aiohttp
import asyncio
import nest_asyncio
nest_asyncio.apply()


async def get(url):
    """
    Request assíncrono de uma url. Se existir site, 
    retorna 1. 
    """
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    return 1
                else:
                    return 0
    except:
        return 0

def monte_carlo(n,k,alphabet):
    """
    Monte Carlo para estimar a quantidade de
    sites que existem em k ou menos letras aleatórias
    no domínio da ufrj.
    """
    trial = []
    for i in range(n):
        num = random.randint(1,k)
        aux = random.sample(alphabet, num)
        trial.append(get('http://www.' + ''.join(aux) + '.ufrj.br')) 
        
    loop = asyncio.get_event_loop() 
    results = loop.run_until_complete(asyncio.gather(*trial)) # Faz o request de uma vez só
    # Note que results será um vetor binário de respostas
    
    cont = 0
    for i in results:
        cont = cont + i
    return cont


# Número de Samples
n = 10000

alphabet = list(string.ascii_lowercase)
eixoX = np.linspace(1, n, 20, dtype = int)
estim_w1 = []

for i in eixoX:
    estim_w1.append(monte_carlo(i, 4, alphabet))

# # Figure Parameters #
fig = plt.figure(figsize = (15,8))
plt.title('Distribuição de n = {} amostras e suas respectivas estimativas'.format(n)) # Title
plt.ylabel('Estimativa') # y label
plt.xlabel('Número de Amostras') # x label
plt.xlim([1, n]) # x limits
plt.xscale('log') 

# Plots
plt.plot(eixoX, estim_w1, color = 'red')
plt.show()