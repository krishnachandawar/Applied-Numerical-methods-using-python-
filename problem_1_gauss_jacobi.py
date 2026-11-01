# ==============================================================================
# Course: CS2807 Numerical Methods - 3rd Sem BCA (Hons)
# Candidate: Krishna H Chandawar | Reg No: 1RUA25BCA0052 | Sec A
# Problem 1: Gauss-Jacobi Iterative Method
# System of equations:
#   9x -  y +  2z =  18
#   2x + 8y -   z =  -5
#    x - 2y + 10z =  21
# Initial guess: x0 = 0, y0 = 0, z0 = 0
# ==============================================================================

def gauss_jacobi(tol=1e-4, max_iter=50):
    x, y, z = 0.0, 0.0, 0.0
    print('=' * 65)
    print('Problem 1: Gauss-Jacobi Iterative Method')
    print('=' * 65)
    print(f'Iteration  0: x = {x:.4f}, y = {y:.4f}, z = {z:.4f}')
    
    for k in range(1, max_iter + 1):
        # Jacobi updates: use values strictly from previous iteration
        x_new = (18.0 + y - 2.0 * z) / 9.0
        y_new = (-5.0 - 2.0 * x + z) / 8.0
        z_new = (21.0 - x + 2.0 * y) / 10.0
        
        print(f'Iteration {k:2d}: x = {x_new:.4f}, y = {y_new:.4f}, z = {z_new:.4f}')
        
        # Convergence criterion
        if max(abs(x_new - x), abs(y_new - y), abs(z_new - z)) < tol:
            print('-' * 65)
            print(f'Convergence achieved at iteration {k} (tol = {tol})')
            print(f'Final Solution: x = {x_new:.4f}, y = {y_new:.4f}, z = {z_new:.4f}')
            print('=' * 65)
            return x_new, y_new, z_new
            
        x, y, z = x_new, y_new, z_new

if __name__ == '__main__':
    gauss_jacobi()
