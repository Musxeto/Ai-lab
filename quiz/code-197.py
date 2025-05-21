import numpy as np

def f(theta):
    return theta * (np.cos(theta) - 1)

def df(theta):
    return (np.cos(theta) - 1) - theta * np.sin(theta)

def g(theta):
    return 0.0

def regula_falsi(a, b, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        fa, fb = f(a), f(b)
        if abs(fb - fa) < 1e-12:
            # Avoid division by very small number
            return None, i
        c = (a * fb - b * fa) / (fb - fa)
        fc = f(c)
        if abs(fc) < tol:
            return c, i+1
        if fa * fc < 0:
            b = c
        else:
            a = c
    return None, max_iter

def newton_raphson(x0, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        fx = f(x0)
        dfx = df(x0)
        if abs(dfx) < 1e-12:
            return None, i 
        x1 = x0 - fx / dfx
        if abs(x1 - x0) < tol:
            return x1, i+1
        x0 = x1
    return None, max_iter

def fixed_point(x0, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        x1 = g(x0)
        if abs(x1 - x0) < tol:
            return x1, i+1
        x0 = x1
    return None, max_iter

rf_root, rf_iter = regula_falsi(0.1, 2)
nr_root, nr_iter = newton_raphson(1.5)
fp_root, fp_iter = fixed_point(0.5)

print("=== Results ===")
if rf_root is not None:
    print(f"Regula Falsi Root: {rf_root:.6f} in {rf_iter} iterations")
    print(f"f(Regula Falsi root) = {f(rf_root):.6e}")
else:
    print(f"Regula Falsi Method did not converge in {rf_iter} iterations")

if nr_root is not None:
    print(f"Newton-Raphson Root: {nr_root:.6f} in {nr_iter} iterations")
    print(f"f(Newton-Raphson root) = {f(nr_root):.6e}")
else:
    print(f"Newton-Raphson Method did not converge in {nr_iter} iterations")

if fp_root is not None:
    print(f"Fixed-Point Root: {fp_root:.6f} in {fp_iter} iterations")
    print(f"f(Fixed-Point root) = {f(fp_root):.6e}")
else:
    print(f"Fixed-Point Method did not converge in {fp_iter} iterations")
