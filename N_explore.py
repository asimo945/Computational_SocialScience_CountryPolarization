import numpy as np

v=[140,94,93,5,14,0,3,3,4,2,2,2,102]

V = np.array(v)
R = V[-1]
A = V[:-1]
pi = np.array([i**2 for i in A])
Fr=0
sigma_pi = sum(pi)
p_square = sum(A)**2

N = p_square/sigma_pi 
N_max = p_square/(Fr+sigma_pi)
N_min = p_square/(Fr**2+sigma_pi)