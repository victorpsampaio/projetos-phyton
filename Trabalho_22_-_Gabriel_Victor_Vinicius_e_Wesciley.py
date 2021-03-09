"""
Alunos: Gabriel Jordão
        Victor Sampaio
        Vinícius Fernandes
        Wesciley Junio
"""

import numpy as np
import math

def derivada(x,y):
    f = (-2*y) + (4*math.exp(-x))
    return f
#CPF primeiro dos 3 ultimos
a0 = 2
k = a0 / 18
def funcHeun(t0,tf,y0,h):
    print("y[ 0 ] = ",y0)
    if(t0 ==tf):
        return y0
    else:
        for i in np.arange(t0,tf,h):
            ## Y(t) prévia
            derivada0 =derivada(i,y0)
            y = y0 +derivada0*h
            ## Correção sem iteração
            ##derivada da predição
            dep = derivada(i+h,y)
            mediaderivada = (derivada0+dep)/2
            y = y0+mediaderivada*h
            ##-------------------------------------------
            y0=y
            print("y[",round(i+h,1),"] = ",y)
            
            
        return y  
    
t0 = 0
tf = 1
h = 0.2
y0 = 2
y = funcHeun(t0,tf,y0,h)
