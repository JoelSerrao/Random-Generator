#Libraries needed
import matplotlib.pyplot as plt
import numpy as np
import math
import time #used for producing random seed values
from collections import namedtuple

#Global declaration of variables
x0 = int(time.time())%10000    # Use this for a random seed value
a = 110351                      # Multiplier
c = 12345                       # Increment
m = 34843546                    # Modulus
n = 1000                        # Length of the random numbers

#Creating a function for the generator
def MCG(a, m, c, x0):
	x = []
	x.append(x0)
	for i in range(n):
		rand = ((a * x[i])+ c) % m
		x.append(rand)
	return x[1:]

seq = MCG(a, m, c, x0)          # Random Integer creation
rndnum = [i/m for i in seq]     # Random number creation

print('Random numbers are:')
for i, (x, r) in enumerate(zip(seq, rndnum)):
    print(f'X{i + 1} = {x}; R{i + 1} = {r}')

######################################################################
#Test for Uniformity Kolmogorov Smirnov
def KS(sequence):
    KS_test = namedtuple('KS_test', ['D_minus', 'D_plus', 'D'])
    
    #1: Rankig the data from small to large
    sorted = np.sort(sequence)
    size = len(sequence)

    #2: Calculate D_plus and D_minus
    D_plus_list = []
    for i in range(1, size + 1):
        D_plus_list.append((i / size) - sorted[i - 1])
    D_plus = np.max(D_plus_list)

    D_minus_list = []
    for i in range(1, size + 1):
        D_minus_list.append(sorted[i - 1] - ((i - 1) / size))
    D_minus = np.max(D_minus_list)

    #3: Evaluate D
    D = max(D_plus, D_minus)

    return KS_test(D_minus, D_plus, D)

D = KS(rndnum)
print('Kolmogorov Smirnov Test:' )
print(D)
########################################################################
# Test for independence using Auto-Correlation 
def autocorrelation(r, i, l):
        AC = namedtuple('Auto_Correlation', ['rho', 'sigma', 'Z0'])

        N = len(r)
        i = i-1
        s = 0
        M = (N - i - l) // l

        for k in range(M + 1):
            s = s + (r[i + (k * l)] * r[i + ((k + 1) * l)])

        rho = (1 / (M + 1)) * s - 0.25
        sigma = math.sqrt((13 * M) + 7) / (12 * (M + 1))
        Z0 = rho / sigma

        return AC(rho, sigma, Z0)

A = autocorrelation(rndnum, 3, 7)
print('\n Auto-Correlation Test results:')
print(A)

##########################################################################
# Histogram 
def build_histogram(arr, title):
  binNo = math.floor(math.sqrt(len(arr))) 
  n, bins, patches = plt.hist(arr, bins=binNo, color='g', density=True)
  plt.title(title)
  plt.xlabel('Value')
  plt.ylabel('Frequency')
  plt.show()
  plt.show()

build_histogram(rndnum, "Histogram for 2.2")