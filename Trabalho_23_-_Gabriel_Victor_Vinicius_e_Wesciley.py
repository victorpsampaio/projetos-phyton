#Gabriel Araújo, Vinicius Fernandes, Victor Prado e Wesciley Junio

import numpy as np
import math

def funcao(t,u):
  return -2*u + 4*math.e**(-t)


h = 0.2
N = 6

t = np.empty(N)
u = np.copy(t)
pm = np.copy(t)
y = np.copy(t)
z = np.copy(t)

t[0] = 0
u[0] = 2
pm[0] = 0

for i in np.arange(N-1):
  t[i+1] = t[i] + h
  pm[i] = (t[i] + t[i+1])/2
  y[i] = u[i] + (h/2)*funcao(t[i],u[i]) 
  u[i+1] = u[i] + (funcao(pm[i],y[i])*h)
  
for i,tt in enumerate(t):
  print("%f %f" % (t[i],u[i]))