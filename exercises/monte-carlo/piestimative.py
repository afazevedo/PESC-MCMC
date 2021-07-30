# -*- coding: utf-8 -*-
"""
# =============================================================================
Author: Amanda Azevedo
Python Version: 3.9.5
Email: afazevedo29@gmail.com
Course: Algoritmos de Monte Carlo e Cadeias de Markov
Date: 26/05/2020
# =============================================================================
"""

#----------------------------------------------------------------------------#
#----------------------------------------------------------------------------#
            # Value of Pi using Matplotlib animation #
#----------------------------------------------------------------------------#
#----------------------------------------------------------------------------#



#----------------------------------------------------------------------------#
            # Imports #
#----------------------------------------------------------------------------#

import numpy as np
import matplotlib
matplotlib.use("TkAgg") 
import matplotlib.pyplot as plt
from matplotlib.pyplot import *

#----------------------------------------------------------------------------#
            # Functions #
#----------------------------------------------------------------------------#

# Function to estimate pi value

def estimativePi(nTrials, radius, infLim, supLim, xCenter, yCenter):
    
    # 1º Generate random nTrials points in the neighborhood given by inferior and superior limits parameters
    XrandCoords = np.random.default_rng().uniform(infLim, supLim, (nTrials,))
    YrandCoords = np.random.default_rng().uniform(infLim, supLim, (nTrials,))
    
    nInside = 0 # We set the number of inner nodes to 0

    for i in range(nTrials):
        x = XrandCoords[i]
        y = YrandCoords[i]
        # # 2º For each trial, we check if the point (x,y) are inside the circle or not
        if (x-xCenter)**2+(y-yCenter)**2 <= radius**2:
            nInside = nInside + 1 # We count the number of points inside the circle
             
    # The estimate pi as we calculated is given by  
    estimatePi = 4*nInside/nTrials
    print("Value of Pi: ", estimatePi)
    return estimatePi

# Function to plot the estimative of pi value 

def plotEstimativePi(nTrials, radius, infLim, supLim, xCenter, yCenter):

    # Initialization
    # fig = figure(figsize=(8, 8), dpi=120)

    nInside = 0 # Initially we set the number of inner nodes to 0
    nDrops = 0 # Initially we set the number of points to 0
    piValue = [] # Array to store pi values
    nDrops_arr = [] # Array to store the number of points 
    insideX = [] # Array to store the coordinate in the x axis of a inside point 
    outsideX = [] # Array to store the coordinate in the x axis of a outside point 
    insideY = [] # Array to store the coordinate in the y axis of a inside point 
    outsideY = [] # Array to store the coordinate in the y axis of a outside point 
    
    # Some checks so the legend labels are only drawn once
    isFirst1 = True
    isFirst2 = True
    
    # First window parameters
    fig1 = plt.figure(1)
    fig1.set_size_inches(6.5, 6.5)
    plt.get_current_fig_manager().window.wm_geometry("+200+100")  # Position of the window
    plt.xlim(infLim, supLim)
    plt.ylim(infLim, supLim) # As we want a circle inside a square
    plt.legend() 

    # Second window parameters
    fig2 = plt.figure(2)
    fig2.set_size_inches(5, 5, forward=True)
    plt.get_current_fig_manager().window.wm_geometry("+1000+250") # move the window
    plt.ylim(0,6.2)
    
    # 1º Generate random nTrials points in the neighborhood given by inferior and superior limits parameters
    XrandCoords = np.random.default_rng().uniform(infLim, supLim, (nTrials,))
    YrandCoords = np.random.default_rng().uniform(infLim, supLim, (nTrials,))

    # Monte Carlo algorithm 
    for i in range(nTrials):
        x = XrandCoords[i]
        y = YrandCoords[i]

        # Increment the counter for number of total pins dropped
        nDrops = nDrops + 1
        
        # For each trial, we check if the point (x,y) are inside the circle or not
        if ((x-xCenter)**2 + (y-yCenter)**2) <= radius**2:
            nInside = nInside + 1
            # If it is inside, we storage the coordinates in the inside arrays
            insideX.append(x)
            insideY.append(y)        
        else:
            # If not, we storage the coordinates in the outside arrays
            outsideX.append(x)
            outsideY.append(y)
            
        if i % 100 == 0:
            #-------------------------------#
                    #First Window 
            #-------------------------------#

            #Ploting the inside points
            plt.figure(1)
            if isFirst1:
                isFirst1 = False
                plt.scatter(insideX, insideY, c='orange', s=50, label='Ponto dentro')
                plt.legend(loc = "best") # In the best position
            else:
                plt.scatter(insideX, insideY, c='orange', s=50, label='Ponto dentro')
            
            # Ploting the outside points
            plt.figure(1)
            if isFirst2:
                isFirst2 = False
                plt.scatter(outsideX,outsideY,c='blue',s=50,label='Ponto fora')
                plt.legend(loc="best") # In the best position
            else:
                plt.scatter(outsideX,outsideY,c='blue',s=50,label='Ponto fora') 
            
            estimatePi = 4*nInside/nDrops
            plt.figure(1)
            # Plotting the title 
            
            plt.title('Número de pontos = '+str(nDrops)+';         \n Número dentro do círculo  = '+str(nInside)+r'; π  ≈ $4\frac{N_\mathrm{dentro}}{N_\mathrm{total}}=$ '+str(np.round(estimatePi,6)) + '\n Valor de pi: ' + str(np.pi))
           
            piValue.append(estimatePi) # We store the actual estimate pi value
            nDrops_arr.append(nDrops) # We store the number of points at that time

            #-------------------------------#
                    #Second Window 
            #-------------------------------#

            plt.figure(2)
            plt.axhline(y=np.pi, c='green',linewidth=2,alpha=0.5)
            plt.plot(nDrops_arr, piValue, c='pink')
            plt.title('Estimativa de π vs Número de pontos')
            plt.annotate('π',[0, np.pi], fontsize=20)
            # The following command is needed to make the second window plot work
            plt.draw()
            # Pause for animation
            plt.pause(0.1)
    
    
    estimatePi = 4*nInside/nTrials
    print("Value of Pi: ", estimatePi)
    plt.show()
    return estimatePi

#----------------------------------------------------------------------------#
            # Input Parameters #
#----------------------------------------------------------------------------#

nTrials = 5000 # number of tentatives
radius = 0.5 # circle radius
infLim = 0 # inferior limit in the x axis
supLim = 1 # superior limit in the x axis
xCenter = 0.5 # value of x coordinate at x axis
yCenter = 0.5 # value of y coordinate at y axis 
fig = figure(figsize=(6, 6), dpi=120) # size of the figure 1


#----------------------------------------------------------------------------#
            # Calling the function #
#----------------------------------------------------------------------------#

# pi = estimativePi(nTrials, radius, infLim, supLim, xCenter, yCenter)
pi = plotEstimativePi(nTrials, radius, infLim, supLim, xCenter, yCenter)


#----------------------------------------------------------------------------#
            # Error Estimative
#----------------------------------------------------------------------------#

# todo