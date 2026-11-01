# ==============================================================================
# Course: CS2807 Numerical Methods - 3rd Sem BCA (Hons)
# Candidate: Krishna H Chandawar | Reg No: 1RUA25BCA0052 | Sec A
# Problem 6: Application of RK2 - Salt Mixture Problem
# ODE: dy/dt = 12 - y/20, y(0) = 0, h = 5 min, Target: y(15)
# Inflow: 4 L/min @ 3 g/L = 12 g/min, Outflow: 4 L/min, Tank Volume: 80 L
# ==============================================================================
import math

def dydt(t, y):
    return 12.0 - y / 20.0

def salt_mixture_rk2(h=5.0, t_end=15.0):
    t, y = 0.0, 0.0
    steps = int(round(t_end / h))
    print('=' * 70)
    print('Problem 6: Application of Runge-Kutta 2nd Order - Salt Mixture')
    print('=' * 70)
    print('Differential Equation: dy/dt = 12 - y/20, y(0) = 0, Step size h = 5.0 min')
    print('-' * 70)
    print(f"{'Step':<6}{'Time t (min)':<14}{'k1 (g)':<14}{'k2 (g)':<14}{'Salt y(t) (g)':<14}")
    print('-' * 70)
    
    for i in range(steps):
        k1 = h * dydt(t, y)
        k2 = h * dydt(t + h, y + k1)
        y_next = y + 0.5 * (k1 + k2)
        t += h
        print(f'{i+1:<6}{t:<14.1f}{k1:<14.4f}{k2:<14.4f}{y_next:<14.4f}')
        y = y_next
        
    print('-' * 70)
    print(f'Estimated salt after {t_end:.0f} minutes: y({t_end:.0f}) = {y:.4f} grams')
    
    # Exact analytical solution for comparison
    exact_salt = 240.0 * (1.0 - math.exp(-t_end / 20.0))
    print(f'Exact analytical solution: y_exact({t_end:.0f}) = {exact_salt:.4f} grams')
    print(f'Absolute relative error: {abs(y - exact_salt) / exact_salt * 100:.2f}%')
    print('=' * 70)
    return y

if __name__ == '__main__':
    salt_mixture_rk2()
