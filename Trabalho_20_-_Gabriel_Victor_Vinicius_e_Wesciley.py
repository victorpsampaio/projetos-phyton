#Gabriel Araújo, Vinicius Fernandes, Victor Prado e Wesciley Junio

import numpy as np
import math


def funcao(t,u):
  return -2*u + 4*math.e**(-t)

h = 0.2
N = 6

t = np.empty(N)
u = np.copy(t)

t[0] = 0
u[0] = 2

for i in np.arange(N-1):
  t[i+1] = t[i] + h
  u[i+1] = u[i] + (funcao(t[i],u[i])*h)

for i,tt in enumerate(t):
  print("%f %f" % (t[i],u[i]))