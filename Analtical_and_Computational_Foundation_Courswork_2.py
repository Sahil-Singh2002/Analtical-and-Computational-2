def secant_method(f,x0,x1,tol,kmax):
    if tol <= 0:
        raise ValueError("Need a positive number as error tolerance!")
    if kmax <=0 or not isinstance(kmax,int):
        raise ValueError("Need a positive integer as bound on the number of iterations.")
    if x0==x1:
        raise ValueError("WHY??? Just WHY")
# this code above makes sure the parameters are valid
    k = 2 
    x_k_1 = x0
    xk = x1
    ek = abs(xk - x_k_1)/abs(xk)
    while ek >= tol:
        if k > kmax:
            raise ArithmeticError
        temp = xk
        xk = (xk) - ((xk -(x_k_1))/(f(xk) - f(x_k_1)))*f(xk) 
        x_k_1 = temp
        k += 1
        ek = abs(xk - x_k_1)/abs(xk)
    return (xk,ek,k)

def secant_method_list(f,x0,x1,tol,kmax):
    # Your code here
    if tol <= 0:
        raise ValueError("Need a positive number as error tolerance!")
    if kmax <=0 or not isinstance(kmax,int):
        raise ValueError("Need a positive integer as bound on the number of iterations.")
    if x0==x1:
        raise ValueError("should not be possible")
# this code above makes sure the parameters are valid
    k = 2 
    x_k_1 = x0
    xk = x1
    ek = abs(xk - x_k_1)/abs(xk)
    x_list = [x0,x1]
    while ek >= tol:
        if k > kmax:
            raise ArithmeticError
        temp = xk
        xk = (xk) - ((xk -(x_k_1))/(f(xk) - f(x_k_1)))*f(xk) 
        x_k_1 = temp
        k += 1
        ek = abs(xk - x_k_1)/abs(xk)
        x_list.append(xk)
    return [(n,f(n)) for n in x_list]

import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return (x**3 -x**2 +2*x +1)/(3*x**2 +2)

root = secant_method_list(f,-2,1,1e-10,100)

fig = plt.figure()
ax=fig.add_subplot(111)

x = np.linspace(-5,5)
y = f(x)

ax.axhline(y=0, color= "k")
ax.axvline(x=0, color= "k")

ax.plot(x,y)
root5 = root[0:5]
ax.scatter([each[0] for each in root5], [each[1] for each in root5])
ax.plot([each[0] for each in root5], [each[1] for each in root5])
ax.set_xlim(-3,1.2)
ax.set_ylim(-1.5,1)
plt.title("Newton’s method")
plt.xlabel("X")
plt.ylabel("Y")

n = 0 
for coord in root[:5]:
    ax.annotate(f'x{n}', xy=coord, textcoords='data')
    n += 1
fig.savefig('outputimage.png')

