"""
Alunos: Gabriel Jordão
        Victor Sampaio
        Vinícius Fernandes
        Wesciley Junio
"""
import numpy as np
import math

def f(x):
    f = math.log(x-5,3)
    return f

def Somaimpar(j):
    fun = 0
    for i in range(0,n,2):
        fun=fun+f(j[i])
    return fun
        
def Somapar(j):
    fun = 0
    for i in range(1,n,2):
        fun=fun+f(j[i])
    return fun

def Fsoma(a,b,n):
    j = np.linspace(a,b,num=n)
    fun = f(a)+3*Somaimpar(j)+2*Somapar(j)+f(b)
    return fun
    
a = 7
b = 17
n = 20
S = Fsoma(a,b,n)

I = (3*(b-a)/(8*n))*(S)
print(I)