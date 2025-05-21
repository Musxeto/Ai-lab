import numpy as np

def f(theta):
    return theta * np.cos(theta) - theta

def df(theta):
    return np.cos(theta) - theta * np.sin(theta) - 1

def g(theta):
    return np.cos(theta)

# Regula Falsi Method
def regula_falsi(a, b, tol=1e-6, max_iter=100):
    iterations = []
    
    if f(a) * f(b) >= 0:
        print("Regula Falsi method requires f(a) and f(b) to have opposite signs.")
        return None, iterations
    
    c = a
    for i in range(max_iter):
        c_old = c
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        iterations.append((i+1, c, f(c)))
        
        if abs(c - c_old) < tol:
            break
            
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
            
    return c, iterations

# Newton-Raphson Method
def newton_raphson(x0, tol=1e-6, max_iter=100):
    iterations = []
    
    x = x0
    for i in range(max_iter):
        fx = f(x)
        iterations.append((i+1, x, fx))
        
        if abs(fx) < tol:
            break
            
        dfx = df(x)
        if abs(dfx) < 1e-10:  # Avoid division by near-zero
            print("Derivative too close to zero.")
            break
            
        x_new = x - fx / dfx
        if abs(x_new - x) < tol:
            x = x_new
            iterations.append((i+2, x, f(x)))
            break
            
        x = x_new
        
    return x, iterations

# Fixed-Point Method
def fixed_point(x0, tol=1e-6, max_iter=100):
    iterations = []
    
    x = x0
    for i in range(max_iter):
        iterations.append((i+1, x, f(x)))
        
        x_new = g(x)
        if abs(x_new - x) < tol:
            x = x_new
            iterations.append((i+2, x, f(x)))
            break
            
        x = x_new
        
    return x, iterations

print("NUMERICAL METHODS RESULTS:\n")

print("REGULA FALSI METHOD:")
a, b = -0.5, 0.5  
root_rf, iter_rf = regula_falsi(a, b)
print(f"Root: {root_rf}")
print("Iterations:")
for iter_num, x, fx in iter_rf:
    print(f"Iteration {iter_num}: x = {x:.10f}, f(x) = {fx:.10e}")
print()

# Newton-Raphson
print("NEWTON-RAPHSON METHOD:")
x0 = 0.5  
root_nr, iter_nr = newton_raphson(x0)
print(f"Root: {root_nr}")
print("Iterations:")
for iter_num, x, fx in iter_nr:
    print(f"Iteration {iter_num}: x = {x:.10f}, f(x) = {fx:.10e}")
print()

# Fixed-Point
print("FIXED-POINT METHOD:")
x0 = 0.5  
root_fp, iter_fp = fixed_point(x0)
print(f"Root: {root_fp}")
print("Iterations:")
for iter_num, x, fx in iter_fp:
    print(f"Iteration {iter_num}: x = {x:.10f}, f(x) = {fx:.10e}")
print()

print("SUMMARY OF RESULTS:")
print(f"Regula Falsi: Root = {root_rf:.10f} in {len(iter_rf)} iterations")
print(f"Newton-Raphson: Root = {root_nr:.10f} in {len(iter_nr)} iterations")
print(f"Fixed-Point: Root = {root_fp:.10f} in {len(iter_fp)} iterations")
print(f"Note: Fixed-Point method converged to {root_fp:.10f}, which is not a true root of the original equation.")