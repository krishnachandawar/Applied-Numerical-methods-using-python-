# ==============================================================================
# Course: CS2807 Numerical Methods - 3rd Sem BCA (Hons)
# Candidate: Krishna H Chandawar | Reg No: 1RUA25BCA0052 | Sec A
# Problem 5: Runge-Kutta 2nd Order (RK2) Method
# ODE: dy/dx = sin(x - y), y(0) = 1, h = 0.1, Compute y(0.3)
# ==============================================================================
import math

def f(x, y):
    return math.sin(x - y)

def rk2_heun(x0=0.0, y0=1.0, h=0.1, x_end=0.3):
    x, y = x0, y0
    steps = int(round((x_end - x0) / h))
    print('=' * 65)
    print('Problem 5: Runge-Kutta 2nd Order (RK2) Method')
    print('=' * 65)
    print(f'ODE: dy/dx = sin(x - y), y({x0}) = {y0}, step size h = {h}')
    print('-' * 65)
    print(f"{'Step':<6}{'x_n':<8}{'k1':<14}{'k2':<14}{'y_(n+1)':<12}")
    print('-' * 65)
    
    for i in range(steps):
        k1 = h * f(x, y)
        k2 = h * f(x + h, y + k1)
        y_next = y + 0.5 * (k1 + k2)
        x = round(x + h, 4)
        print(f'{i+1:<6}{x:<8.2f}{k1:<14.6f}{k2:<14.6f}{y_next:<12.6f}')
        y = y_next
        
    print('-' * 65)
    print(f'Final estimated y({x_end}) = {y:.4f}')
    print('=' * 65)
    return y

if __name__ == '__main__':
    rk2_heun()
