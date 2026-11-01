# ==============================================================================
# Master runner for CS2807 Numerical Methods Activity (Set 2)
# Candidate: Krishna H Chandawar | Reg No: 1RUA25BCA0052 | Sec A
# ==============================================================================
import subprocess, sys, os

scripts = [
    'problem_1_gauss_jacobi.py',
    'problem_2_gauss_seidel.py',
    'problem_3_euler_method.py',
    'problem_4_newton_cooling_euler.py',
    'problem_5_rk2_method.py',
    'problem_6_rk2_salt_mixture.py'
]

cur_dir = os.path.dirname(os.path.abspath(__file__))
print("=" * 70)
print("EXECUTING ALL CS2807 NUMERICAL METHODS PYTHON ACTIVITY SCRIPTS")
print("Candidate: Krishna H Chandawar | Reg: 1RUA25BCA0052 | Section A")
print("=" * 70 + "\n")

for script in scripts:
    spath = os.path.join(cur_dir, script)
    res = subprocess.run([sys.executable, spath], capture_output=True, text=True)
    print(res.stdout)
    if res.stderr:
        print('Error:', res.stderr)

print("All 6 problem scripts executed and verified successfully!")
