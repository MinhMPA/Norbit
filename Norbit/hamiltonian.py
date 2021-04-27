import numpy as np
import numba as nb
NUMBA_NUM_THREADS="16"

__all__ = ['dVdq', 'f']

# Physical constants
G = 2.95912208286E-4 # gravitational constant

@nb.jit
def dVdq(q,mass):
    dVdq = np.zeros_like(q)
    for i in nb.prange(mass.shape[0]):
        for j in nb.prange(mass.shape[0]):
            if (i!=j):
                r = q[i,:]-q[j,:]
                r = np.sqrt(r.dot(r))
                dVdq[i,:] -= (G*mass[j])*(q[i,:]-q[j,:]) / (r**3)
    return dVdq

@nb.jit
def f(w,mass):
    f = np.zeros_like(w)
    f[0,...] = w[1,...]
    for i in nb.prange(mass.shape[0]):
        for j in nb.prange(mass.shape[0]):
            if (i!=j):
                r = w[0,i,:]-w[0,j,:]
                r = np.sqrt(r.dot(r))
                f[1,i,:] -= (G*mass[j])*(w[0,i,:]-w[0,j,:]) / (r**3)
    return f
