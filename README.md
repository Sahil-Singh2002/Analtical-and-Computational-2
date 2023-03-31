# Analtical and Computational 2

**Introdunction**

The Secant Method can be used to find a root, *x*, of a function f(x) so that *f(x*)=0. This method is an adaptation of Newton’s method, where the derivative is estimated using the approximation f'(xk)≃ {f(xk)−f(xk−1)}/xk−xk−1.In the Secant Method a sequence of successive estimates for *x*, labelled {xk}k≥1, are calculated using the formula x_(k+1)=x_k − {x_k−x_(k−1)/f(x_k)−f(x_(k−1))}f(xk). Geometrically x_(k+1) is obtained from x_k and x_(k−1) by intersecting the straight line through (x_k,f(x_k)) and (x_(k+1),f(x_(k+1))) with the x-axis. Since each calculation of the new estimate, x_(k+1), requires the values of the previous two estimates, x_(k) and x_(k−1), we must specify x_0 and x_1 initially, choosing values that are close to the root we seek. Ideally, we should choose x_0 and x_1 in a similar way to the initial endpoints of an interval for the bisection method, such that f(x)=0 precisely once in the interval (x_0,x_1), though this is not necessary for the secant method to work. 

**CODE**

* The function secant_method below which takes as input a function f, two real numbers x_0 and x_1, a positive real number tol and a positive integer kmax. This function should implement the Secant Method to find a root of a function f using the two starting points x_0 and x_1. Successive estimates should be calculated until the relative error e_k is less than tol or k>kmax.
* The function secant_method_list is the updated function which just out puts list of approximations.
* Using the function secant_method_list from the function above, with initial approximations x_0= −2 and x_1=1 to compute a list of approximations, x_0,x_1,…,x_N to the unique real zero of f (which lies between x_0 and x_1). Illustrate the Secant Method by plotting the curve of f, the x-axis, the five points z_i=(x_i,f(x_i)) for 0≤i≤4 on the curve, the four straight lines (secants) between z_0 and z_1, z_1 and z_2, z_2 and z_3, and z_3 and z_4. The plot should have size (20,10) and be limited in both x and y -directions in such a way that the relevant parts of the graphs and intersections are clearly visible. The function f is defined to be f(x) = x^3−x^2+2x+1/3x^2+2.

**Conclusion**

The first function is our main function which is the algorithm of the Secant Method while the other two codes are to help display how the convergence takes place as showen primirly in graph for the third code.
