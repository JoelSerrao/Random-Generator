#Libraries needed
import numpy as np
import time #used for producing random seed values

#Global declaration of variables
x0 = int(time.time())%10000     # Use this for a random seed value
a = 110351                      # Multiplier
c = 12345                       # Increment
m = 34843546                    # Modulus
n = 1000                        # Length of the random numbers

#Creating a function for the generator
def MCG(a, m, c, x0, n):
    x = []
    x.append(x0)
    for i in range(n):
        rand = ((a * x[i]) + c) % m
        x.append(rand)
    return x[1:]

#Using the piecewise conditions to get random variates
def RndVar(R):
    if R <= 1/3:
        rv = 1/3 * np.log(3*R)
    else:
        rv = -1/3 * np.log(3 - 3 * R)
    return rv


seq = MCG(a, m, c, x0, n)               # Random Integer creation
rndnum = [i/m for i in seq]             # Random number creation
rndvar = [RndVar(r) for r in rndnum]    # Random variate creation

print('Random Variates are RV(i):')
for i, (x, r, rv) in enumerate(zip(seq, rndnum, rndvar)):
    print(f'X{i + 1} = {x}; R{i + 1} = {r}; RV{i + 1} = {rv}')
