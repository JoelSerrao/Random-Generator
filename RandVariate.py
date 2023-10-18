#Libraries needed
import numpy as np

#Global declaration of variables
x0 = 37         # Seed
a = 7           # Multiplier 
c = 29          # Increment
m = 100         # Modulus 
n = m-1         # Length of random numbers

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
