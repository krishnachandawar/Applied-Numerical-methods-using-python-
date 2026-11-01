# ==============================================================================
# Course: CS2807 Numerical Methods - 3rd Sem BCA (Hons)
# Candidate: Krishna H Chandawar | Reg No: 1RUA25BCA0052 | Sec A
# Problem 3: Euler's Method for ODE
# ODE: dy/dx = x + y^2, y(0) = 1, h = 0.1, Compute y(0.1), y(0.2), y(0.3)
# ==============================================================================

def f(x, y):
    return x + y**2

def euler(x0=0.0, y0=1.0, h=0.1, x_end=0.3):
    steps = int(round((x_end - x0) / h))
    x, y = x0, y0
    print('=' * 65)
    print("Problem 3: Euler's Method for ODE")
    print('=' * 65)
    print(f'Initial Condition: x0 = {x0:.1f}, y0 = {y0:.4f}, Step size h = {h}')
    print('-' * 65)
    print(f"{'Step':<6}{'x_n':<10}{'y_n':<14}{'f(x_n, y_n)':<16}{'y_(n+1)':<12}")
    print('-' * 65)
    
    for i in range(steps):
        slope = f(x, y)
        y_next = y + h * slope
        print(f'{i+1:<6}{x:<10.2f}{y:<14.4f}{slope:<16.6f}{y_next:<12.4f}')
        x = round(x + h, 4)
        y = y_next
        
    print('-' * 65)
    print(f'Final estimated y({x_end}) = {y:.4f}')
    print('=' * 65)
    return y

if __name__ == '__main__':
    euler()
