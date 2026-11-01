# ==============================================================================
# Course: CS2807 Numerical Methods - 3rd Sem BCA (Hons)
# Candidate: Krishna H Chandawar | Reg No: 1RUA25BCA0052 | Sec A
# Problem 4: Application of Euler's Method - Newton's Law of Cooling
# ODE: dT/dt = -k*(T - Ta), k = 0.05 /min, Ta = 20 C, T(0) = 90 C, h = 4 min
# Target: Temperature after 8 minutes (t = 8 min)
# ==============================================================================

def newtons_cooling_euler(k=0.05, Ta=20.0, T0=90.0, h=4.0, t_end=8.0):
    t, T = 0.0, T0
    steps = int(round(t_end / h))
    print('=' * 65)
    print("Problem 4: Newton's Law of Cooling using Euler's Method")
    print('=' * 65)
    print(f'Parameters: k = {k}/min, Ta = {Ta} C, T(0) = {T0} C, h = {h} min')
    print('-' * 65)
    print(f"{'Step':<6}{'Time t (min)':<15}{'Current T (C)':<16}{'dT/dt (C/min)':<16}{'Next T (C)':<12}")
    print('-' * 65)
    
    for i in range(steps):
        rate = -k * (T - Ta)
        T_next = T + h * rate
        print(f'{i+1:<6}{t:<15.1f}{T:<16.2f}{rate:<16.2f}{T_next:<12.2f}')
        t += h
        T = T_next
        
    print('-' * 65)
    print(f'Estimated temperature after {t_end:.0f} minutes: T({t_end:.0f}) = {T:.2f} C')
    print('=' * 65)
    return T

if __name__ == '__main__':
    newtons_cooling_euler()
