import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def create_report():
    doc = Document()

    # Set margins
    for section in doc.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)

    scratch_dir = r"C:\Users\chand\.gemini\antigravity\scratch"
    logo_path = os.path.join(scratch_dir, "logo_0.png")

    # ------------------ COVER PAGE ------------------
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("CIE-3-Coding Based Activity\n")
    r.bold = True
    r.font.size = Pt(18)
    r.font.name = "Arial"

    p_proj = doc.add_paragraph()
    p_proj.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p_proj.add_run("A PROJECT REPORT\n\nSubmitted by\n")
    r.bold = True
    r.font.size = Pt(14)
    r.font.name = "Arial"

    p_cand = doc.add_paragraph()
    p_cand.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_name = p_cand.add_run("KRISHNA H CHANDAWAR\n")
    r_name.bold = True
    r_name.font.size = Pt(16)
    r_name.font.color.rgb = RGBColor(192, 0, 0)
    r_name.font.name = "Arial"

    r_reg = p_cand.add_run("Register No: 1RUA25BCA0052\nSection: Section A\n\n")
    r_reg.bold = True
    r_reg.font.size = Pt(13)
    r_reg.font.name = "Arial"

    p_eval = doc.add_paragraph()
    p_eval.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_eval = p_eval.add_run("as part of the Continuous Internal Evaluation\nfor the course\n\n")
    r_eval.italic = True
    r_eval.font.size = Pt(13)
    r_eval.font.name = "Arial"

    r_course = p_eval.add_run("CS2807 Numerical Methods\n\n")
    r_course.bold = True
    r_course.font.size = Pt(16)
    r_course.font.name = "Arial"

    r_sem = p_eval.add_run("Offered in\nSemester III\nof\nBCA (Hons)\n\n")
    r_sem.font.size = Pt(13)
    r_sem.font.name = "Arial"

    if os.path.exists(logo_path):
        p_logo = doc.add_paragraph()
        p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo.add_run().add_picture(logo_path, width=Inches(2.5))

    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_inst = p_inst.add_run("\nSchool of Computer Science and Engineering\nRV University\nRV Vidyaniketan, 8th Mile, Mysore Road, Bengaluru, Karnataka, India - 560059\n\n")
    r_inst.bold = True
    r_inst.font.size = Pt(12)
    r_inst.font.name = "Arial"

    r_date = p_inst.add_run("NOVEMBER 2026")
    r_date.bold = True
    r_date.font.size = Pt(13)
    r_date.font.color.rgb = RGBColor(192, 0, 0)
    r_date.font.name = "Arial"

    doc.add_page_break()

    # ------------------ PROBLEMS SECTION ------------------
    def add_heading_styled(text, level=1):
        h = doc.add_heading(text, level=level)
        h.paragraph_format.space_before = Pt(14)
        h.paragraph_format.space_after = Pt(6)
        for r in h.runs:
            r.font.name = "Arial"
            r.font.color.rgb = RGBColor(0, 51, 102)
        return h

    def add_code_block(code_text):
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl.autofit = False
        cell = tbl.cell(0, 0)
        cell.width = Inches(6.5)
        
        # Light grey background
        shd = parse_xml(r'<w:shd {} w:fill="F4F4F4"/>'.format(nsdecls('w')))
        cell._tc.get_or_add_tcPr().append(shd)
        
        # Border
        borders = parse_xml(r'<w:tcBorders {}><w:top w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/><w:left w:val="single" w:sz="12" w:space="0" w:color="003366"/><w:bottom w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/><w:right w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/></w:tcBorders>'.format(nsdecls('w')))
        cell._tc.get_or_add_tcPr().append(borders)

        cp = cell.paragraphs[0]
        cp.paragraph_format.space_before = Pt(4)
        cp.paragraph_format.space_after = Pt(4)
        r = cp.add_run(code_text)
        r.font.name = "Consolas"
        r.font.size = Pt(9.5)
        r.font.color.rgb = RGBColor(34, 34, 34)

    def add_output_block(out_text):
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl.autofit = False
        cell = tbl.cell(0, 0)
        cell.width = Inches(6.5)

        shd = parse_xml(r'<w:shd {} w:fill="EBF2F7"/>'.format(nsdecls('w')))
        cell._tc.get_or_add_tcPr().append(shd)

        borders = parse_xml(r'<w:tcBorders {}><w:top w:val="single" w:sz="4" w:space="0" w:color="B0C4DE"/><w:left w:val="single" w:sz="12" w:space="0" w:color="2E8B57"/><w:bottom w:val="single" w:sz="4" w:space="0" w:color="B0C4DE"/><w:right w:val="single" w:sz="4" w:space="0" w:color="B0C4DE"/></w:tcBorders>'.format(nsdecls('w')))
        cell._tc.get_or_add_tcPr().append(borders)

        cp = cell.paragraphs[0]
        cp.paragraph_format.space_before = Pt(4)
        cp.paragraph_format.space_after = Pt(4)
        r = cp.add_run(out_text)
        r.font.name = "Consolas"
        r.font.size = Pt(9.5)
        r.font.color.rgb = RGBColor(0, 51, 0)

    # ------------------ PROBLEM 1 ------------------
    add_heading_styled("1. Problem - 1: Gauss–Jacobi Iterative Method", level=1)
    
    p = doc.add_paragraph()
    r = p.add_run("Problem Statement:\n")
    r.bold = True
    p.add_run("Solve the following system of linear equations using the Gauss–Jacobi iterative method up to four decimal places:\n"
              "    9x - y + 2z = 18\n"
              "    2x + 8y - z = -5\n"
              "    x - 2y + 10z = 21\n"
              "Use the initial guess: x^(0) = 0, y^(0) = 0, z^(0) = 0.")

    p = doc.add_paragraph()
    r = p.add_run("Manual Solution:")
    r.bold = True
    
    p = doc.add_paragraph()
    p.add_run("Step 1: Check for Diagonal Dominance\n"
              "• For equation 1: |9| = 9 > |-1| + |2| = 3  (True)\n"
              "• For equation 2: |8| = 8 > |2| + |-1| = 3  (True)\n"
              "• For equation 3: |10| = 10 > |1| + |-2| = 3 (True)\n"
              "Since the coefficient matrix is strictly diagonally dominant, convergence of the Gauss–Jacobi method is guaranteed.\n\n"
              "Step 2: Express Iterative Formulas\n"
              "Rewriting each equation for the diagonal variable:\n"
              "    x^(k+1) = (18 + y^(k) - 2z^(k)) / 9\n"
              "    y^(k+1) = (-5 - 2x^(k) + z^(k)) / 8\n"
              "    z^(k+1) = (21 - x^(k) + 2y^(k)) / 10\n\n"
              "Step 3: Perform Iterations (Initial Guess: x^(0) = 0, y^(0) = 0, z^(0) = 0)\n\n"
              "• Iteration 1 (k = 0):\n"
              "  x^(1) = (18 + 0 - 2(0)) / 9 = 18 / 9 = 2.0000\n"
              "  y^(1) = (-5 - 2(0) + 0) / 8 = -5 / 8 = -0.6250\n"
              "  z^(1) = (21 - 0 + 2(0)) / 10 = 21 / 10 = 2.1000\n\n"
              "• Iteration 2 (k = 1):\n"
              "  x^(2) = (18 + (-0.6250) - 2(2.1000)) / 9 = (18 - 0.6250 - 4.2000) / 9 = 13.1750 / 9 ≈ 1.4639\n"
              "  y^(2) = (-5 - 2(2.0000) + 2.1000) / 8 = (-5 - 4.0000 + 2.1000) / 8 = -6.9000 / 8 = -0.8625\n"
              "  z^(2) = (21 - 2.0000 + 2(-0.6250)) / 10 = (21 - 2.0000 - 1.2500) / 10 = 17.7500 / 10 = 1.7750\n\n"
              "• Iteration 3 (k = 2):\n"
              "  x^(3) = (18 + (-0.8625) - 2(1.7750)) / 9 = 13.5875 / 9 ≈ 1.5097\n"
              "  y^(3) = (-5 - 2(1.4639) + 1.7750) / 8 = -6.1528 / 8 ≈ -0.7691\n"
              "  z^(3) = (21 - 1.4639 + 2(-0.8625)) / 10 = 17.8111 / 10 ≈ 1.7811\n\n"
              "• Iteration 4 (k = 3):\n"
              "  x^(4) = (18 + (-0.7691) - 2(1.7811)) / 9 = 13.6687 / 9 ≈ 1.5187\n"
              "  y^(4) = (-5 - 2(1.5097) + 1.7811) / 8 = -6.2383 / 8 ≈ -0.7798\n"
              "  z^(4) = (21 - 1.5097 + 2(-0.7691)) / 10 = 17.9521 / 10 ≈ 1.7952\n\n"
              "• Iteration 5 (k = 4):\n"
              "  x^(5) = (18 + (-0.7798) - 2(1.7952)) / 9 = 13.6298 / 9 ≈ 1.5144\n"
              "  y^(5) = (-5 - 2(1.5187) + 1.7952) / 8 = -6.2422 / 8 ≈ -0.7803\n"
              "  z^(5) = (21 - 1.5187 + 2(-0.7798)) / 10 = 17.9217 / 10 ≈ 1.7922\n\n"
              "• Iteration 6 (k = 5):\n"
              "  x^(6) = (18 + (-0.7803) - 2(1.7922)) / 9 = 13.6353 / 9 ≈ 1.5150\n"
              "  y^(6) = (-5 - 2(1.5144) + 1.7922) / 8 = -6.2366 / 8 ≈ -0.7796\n"
              "  z^(6) = (21 - 1.5144 + 2(-0.7803)) / 10 = 17.9250 / 10 ≈ 1.7925\n\n"
              "• Iteration 7 (k = 6):\n"
              "  x^(7) = (18 + (-0.7796) - 2(1.7925)) / 9 = 13.6354 / 9 ≈ 1.5150\n"
              "  y^(7) = (-5 - 2(1.5150) + 1.7925) / 8 = -6.2375 / 8 ≈ -0.7797\n"
              "  z^(7) = (21 - 1.5150 + 2(-0.7796)) / 10 = 17.9258 / 10 ≈ 1.7926\n\n"
              "• Iteration 8 (k = 7):\n"
              "  x^(8) = 1.5150,  y^(8) = -0.7797,  z^(8) = 1.7926\n\n"
              "Final Solution (correct to 4 decimal places):\n"
              "    x = 1.5150,  y = -0.7797,  z = 1.7926")

    p = doc.add_paragraph()
    r = p.add_run("Python Program:")
    r.bold = True
    
    code_q1 = '''# ==============================================================================
# Problem 1: Gauss-Jacobi Iterative Method
# System:
#   9x -  y +  2z =  18
#   2x + 8y -   z =  -5
#    x - 2y + 10z =  21
# ==============================================================================

def gauss_jacobi(tol=1e-4, max_iter=50):
    # Initial approximations
    x, y, z = 0.0, 0.0, 0.0
    print("Iteration 0: x = {:.4f}, y = {:.4f}, z = {:.4f}".format(x, y, z))
    
    for k in range(1, max_iter + 1):
        # Gauss-Jacobi update formulas using values from previous iteration
        x_new = (18.0 + y - 2.0 * z) / 9.0
        y_new = (-5.0 - 2.0 * x + z) / 8.0
        z_new = (21.0 - x + 2.0 * y) / 10.0
        
        print(f"Iteration {k:2d}: x = {x_new:.4f}, y = {y_new:.4f}, z = {z_new:.4f}")
        
        # Check convergence criterion up to 4 decimal places
        if max(abs(x_new - x), abs(y_new - y), abs(z_new - z)) < tol:
            print(f"\\nConvergence achieved at iteration {k}!")
            print(f"Final Solution: x = {x_new:.4f}, y = {y_new:.4f}, z = {z_new:.4f}")
            break
            
        x, y, z = x_new, y_new, z_new

if __name__ == "__main__":
    gauss_jacobi()'''
    add_code_block(code_q1)

    p = doc.add_paragraph()
    r = p.add_run("OUTPUT:")
    r.bold = True

    out_q1 = '''Iteration 0: x = 0.0000, y = 0.0000, z = 0.0000
Iteration  1: x = 2.0000, y = -0.6250, z = 2.1000
Iteration  2: x = 1.4639, y = -0.8625, z = 1.7750
Iteration  3: x = 1.5097, y = -0.7691, z = 1.7811
Iteration  4: x = 1.5187, y = -0.7798, z = 1.7952
Iteration  5: x = 1.5144, y = -0.7803, z = 1.7922
Iteration  6: x = 1.5150, y = -0.7796, z = 1.7925
Iteration  7: x = 1.5150, y = -0.7797, z = 1.7926
Iteration  8: x = 1.5150, y = -0.7797, z = 1.7926

Convergence achieved at iteration 8!
Final Solution: x = 1.5150, y = -0.7797, z = 1.7926'''
    add_output_block(out_q1)

    # ------------------ PROBLEM 2 ------------------
    add_heading_styled("2. Problem - 2: Gauss–Seidel Method", level=1)
    
    p = doc.add_paragraph()
    r = p.add_run("Problem Statement:\n")
    r.bold = True
    p.add_run("Solve the following system of linear equations using the Gauss–Seidel method up to four decimal places:\n"
              "    5x + y - z = 10\n"
              "    -x + 6y + 2z = -2\n"
              "    2x - y + 7z = 9\n"
              "Take the initial guesses: x^(0) = 0, y^(0) = 0, z^(0) = 0.")

    p = doc.add_paragraph()
    r = p.add_run("Manual Solution:")
    r.bold = True
    
    p = doc.add_paragraph()
    p.add_run("Step 1: Check for Diagonal Dominance\n"
              "• For equation 1: |5| = 5 > |1| + |-1| = 2   (True)\n"
              "• For equation 2: |6| = 6 > |-1| + |2| = 3   (True)\n"
              "• For equation 3: |7| = 7 > |2| + |-1| = 3   (True)\n"
              "The system is strictly diagonally dominant, guaranteeing convergence.\n\n"
              "Step 2: Express Iterative Formulas (Gauss–Seidel immediately incorporates freshly computed variables):\n"
              "    x^(k+1) = (10 - y^(k) + z^(k)) / 5\n"
              "    y^(k+1) = (-2 + x^(k+1) - 2z^(k)) / 6\n"
              "    z^(k+1) = (9 - 2x^(k+1) + y^(k+1)) / 7\n\n"
              "Step 3: Perform Iterations (Initial Guess: x^(0) = 0, y^(0) = 0, z^(0) = 0)\n\n"
              "• Iteration 1 (k = 0):\n"
              "  x^(1) = (10 - 0 + 0) / 5 = 10 / 5 = 2.0000\n"
              "  y^(1) = (-2 + 2.0000 - 2(0)) / 6 = 0 / 6 = 0.0000\n"
              "  z^(1) = (9 - 2(2.0000) + 0.0000) / 7 = 5 / 7 ≈ 0.7143\n\n"
              "• Iteration 2 (k = 1):\n"
              "  x^(2) = (10 - 0.0000 + 0.7143) / 5 = 10.7143 / 5 ≈ 2.1429\n"
              "  y^(2) = (-2 + 2.1429 - 2(0.7143)) / 6 = (-2 + 2.1429 - 1.4286) / 6 = -1.2857 / 6 ≈ -0.2143\n"
              "  z^(2) = (9 - 2(2.1429) + (-0.2143)) / 7 = (9 - 4.2858 - 0.2143) / 7 = 4.4999 / 7 ≈ 0.6429\n\n"
              "• Iteration 3 (k = 2):\n"
              "  x^(3) = (10 - (-0.2143) + 0.6429) / 5 = 10.8572 / 5 ≈ 2.1714\n"
              "  y^(3) = (-2 + 2.1714 - 2(0.6429)) / 6 = -1.1144 / 6 ≈ -0.1857\n"
              "  z^(3) = (9 - 2(2.1714) + (-0.1857)) / 7 = 4.4715 / 7 ≈ 0.6388\n\n"
              "• Iteration 4 (k = 3):\n"
              "  x^(4) = (10 - (-0.1857) + 0.6388) / 5 = 10.8245 / 5 ≈ 2.1649\n"
              "  y^(4) = (-2 + 2.1649 - 2(0.6388)) / 6 = -1.1127 / 6 ≈ -0.1854\n"
              "  z^(4) = (9 - 2(2.1649) + (-0.1854)) / 7 = 4.4848 / 7 ≈ 0.6407\n\n"
              "• Iteration 5 (k = 4):\n"
              "  x^(5) = (10 - (-0.1854) + 0.6407) / 5 = 10.8261 / 5 ≈ 2.1652\n"
              "  y^(5) = (-2 + 2.1652 - 2(0.6407)) / 6 = -1.1162 / 6 ≈ -0.1860\n"
              "  z^(5) = (9 - 2(2.1652) + (-0.1860)) / 7 = 4.4836 / 7 ≈ 0.6405\n\n"
              "• Iteration 6 (k = 5):\n"
              "  x^(6) = (10 - (-0.1860) + 0.6405) / 5 = 10.8265 / 5 ≈ 2.1653\n"
              "  y^(6) = (-2 + 2.1653 - 2(0.6405)) / 6 = -1.1157 / 6 ≈ -0.1860\n"
              "  z^(6) = (9 - 2(2.1653) + (-0.1860)) / 7 = 4.4834 / 7 ≈ 0.6405\n\n"
              "Final Solution (correct to 4 decimal places):\n"
              "    x = 2.1653,  y = -0.1860,  z = 0.6405")

    p = doc.add_paragraph()
    r = p.add_run("Python Program:")
    r.bold = True
    
    code_q2 = '''# ==============================================================================
# Problem 2: Gauss-Seidel Iterative Method
# System:
#    5x +  y -  z =  10
#   - x + 6y + 2z =  -2
#    2x -  y + 7z =   9
# ==============================================================================

def gauss_seidel(tol=1e-4, max_iter=50):
    # Initial approximations
    x, y, z = 0.0, 0.0, 0.0
    print("Iteration 0: x = {:.4f}, y = {:.4f}, z = {:.4f}".format(x, y, z))
    
    for k in range(1, max_iter + 1):
        x_old, y_old, z_old = x, y, z
        
        # Gauss-Seidel updates use latest available values immediately
        x = (10.0 - y + z) / 5.0
        y = (-2.0 + x - 2.0 * z) / 6.0
        z = (9.0 - 2.0 * x + y) / 7.0
        
        print(f"Iteration {k:2d}: x = {x:.4f}, y = {y:.4f}, z = {z:.4f}")
        
        # Check convergence condition
        if max(abs(x - x_old), abs(y - y_old), abs(z - z_old)) < tol:
            print(f"\\nConvergence achieved at iteration {k}!")
            print(f"Final Solution: x = {x:.4f}, y = {y:.4f}, z = {z:.4f}")
            break

if __name__ == "__main__":
    gauss_seidel()'''
    add_code_block(code_q2)

    p = doc.add_paragraph()
    r = p.add_run("OUTPUT:")
    r.bold = True

    out_q2 = '''Iteration 0: x = 0.0000, y = 0.0000, z = 0.0000
Iteration  1: x = 2.0000, y = 0.0000, z = 0.7143
Iteration  2: x = 2.1429, y = -0.2143, z = 0.6429
Iteration  3: x = 2.1714, y = -0.1857, z = 0.6388
Iteration  4: x = 2.1649, y = -0.1854, z = 0.6407
Iteration  5: x = 2.1652, y = -0.1860, z = 0.6405
Iteration  6: x = 2.1653, y = -0.1860, z = 0.6405

Convergence achieved at iteration 6!
Final Solution: x = 2.1653, y = -0.1860, z = 0.6405'''
    add_output_block(out_q2)

    # ------------------ PROBLEM 3 ------------------
    add_heading_styled("3. Problem - 3: Euler’s Method", level=1)
    
    p = doc.add_paragraph()
    r = p.add_run("Problem Statement:\n")
    r.bold = True
    p.add_run("Using Euler’s method with step size h = 0.1, estimate y(0.3) for the differential equation:\n"
              "    dy/dx = x + y^2,\n"
              "given y(0) = 1. Compute y(0.1), y(0.2), and y(0.3).")

    p = doc.add_paragraph()
    r = p.add_run("Manual Solution:")
    r.bold = True
    
    p = doc.add_paragraph()
    p.add_run("Given:\n"
              "    f(x, y) = dy/dx = x + y^2\n"
              "    Initial condition: x_0 = 0, y_0 = 1\n"
              "    Step size: h = 0.1\n\n"
              "Euler's Iterative Formula:\n"
              "    y_(n+1) = y_n + h * f(x_n, y_n)\n\n"
              "Step 1: Compute y(0.1) (n = 0):\n"
              "  x_0 = 0,  y_0 = 1\n"
              "  f(x_0, y_0) = 0 + (1)^2 = 1.0\n"
              "  y_1 = y(0.1) = y_0 + h * f(x_0, y_0)\n"
              "               = 1 + 0.1 * (1.0) = 1 + 0.1 = 1.1000\n\n"
              "Step 2: Compute y(0.2) (n = 1):\n"
              "  x_1 = 0.1,  y_1 = 1.1\n"
              "  f(x_1, y_1) = 0.1 + (1.1)^2 = 0.1 + 1.21 = 1.3100\n"
              "  y_2 = y(0.2) = y_1 + h * f(x_1, y_1)\n"
              "               = 1.1 + 0.1 * (1.3100) = 1.1 + 0.1310 = 1.2310\n\n"
              "Step 3: Compute y(0.3) (n = 2):\n"
              "  x_2 = 0.2,  y_2 = 1.231\n"
              "  f(x_2, y_2) = 0.2 + (1.231)^2 = 0.2 + 1.515361 = 1.715361\n"
              "  y_3 = y(0.3) = y_2 + h * f(x_2, y_2)\n"
              "               = 1.231 + 0.1 * (1.715361) = 1.231 + 0.1715361 = 1.4025361 ≈ 1.4025\n\n"
              "Final Results:\n"
              "    y(0.1) = 1.1000\n"
              "    y(0.2) = 1.2310\n"
              "    y(0.3) ≈ 1.4025")

    p = doc.add_paragraph()
    r = p.add_run("Python Program:")
    r.bold = True
    
    code_q3 = '''# ==============================================================================
# Problem 3: Euler's Method for ODE
# ODE: dy/dx = x + y^2, y(0) = 1, h = 0.1, Target: y(0.3)
# ==============================================================================

def f(x, y):
    """Derivative function dy/dx = x + y^2"""
    return x + y**2

def euler_method(x0, y0, h, x_end):
    print(f"Initial Condition: x0 = {x0:.1f}, y0 = {y0:.4f}, step size h = {h}")
    print("-" * 55)
    print(f"{'Step':<6}{'x_n':<10}{'y_n':<12}{'f(x_n, y_n)':<15}{'y_(n+1)':<12}")
    print("-" * 55)
    
    steps = int(round((x_end - x0) / h))
    x, y = x0, y0
    
    for i in range(steps):
        slope = f(x, y)
        y_next = y + h * slope
        print(f"{i+1:<6}{x:<10.2f}{y:<12.4f}{slope:<15.6f}{y_next:<12.4f}")
        x = round(x + h, 4)
        y = y_next
        
    print("-" * 55)
    print(f"Final estimated y({x_end}) = {y:.4f}")

if __name__ == "__main__":
    euler_method(x0=0.0, y0=1.0, h=0.1, x_end=0.3)'''
    add_code_block(code_q3)

    p = doc.add_paragraph()
    r = p.add_run("OUTPUT:")
    r.bold = True

    out_q3 = '''Initial Condition: x0 = 0.0, y0 = 1.0000, step size h = 0.1
-------------------------------------------------------
Step  x_n       y_n         f(x_n, y_n)    y_(n+1)     
-------------------------------------------------------
1     0.00      1.0000      1.000000       1.1000      
2     0.10      1.1000      1.310000       1.2310      
3     0.20      1.2310      1.715361       1.4025      
-------------------------------------------------------
Final estimated y(0.3) = 1.4025'''
    add_output_block(out_q3)

    # ------------------ PROBLEM 4 ------------------
    add_heading_styled("4. Problem - 4: Application of Euler’s Method: Newton’s Law of Cooling", level=1)
    
    p = doc.add_paragraph()
    r = p.add_run("Problem Statement:\n")
    r.bold = True
    p.add_run("The temperature T of a hot object placed in a room satisfies Newton’s Law of Cooling:\n"
              "    dT/dt = -k(T - T_a),\n"
              "where k = 0.05 per minute and the ambient temperature is T_a = 20°C.\n"
              "If the initial temperature of the object is T(0) = 90°C, use Euler’s method with step size h = 4 minutes "
              "to estimate the temperature after 8 minutes.")

    p = doc.add_paragraph()
    r = p.add_run("Manual Solution:")
    r.bold = True
    
    p = doc.add_paragraph()
    p.add_run("Given:\n"
              "    dT/dt = -0.05 * (T - 20)\n"
              "    Initial temperature: T(0) = 90°C (t_0 = 0, T_0 = 90)\n"
              "    Step size: h = 4 minutes\n"
              "    Target time: t = 8 minutes (Number of steps = 8 / 4 = 2 steps)\n\n"
              "Euler's Formula for Temperature:\n"
              "    T_(n+1) = T_n + h * f(t_n, T_n)\n"
              "where f(t, T) = -0.05 * (T - 20).\n\n"
              "Step 1: At t = 0 min to estimate T(4) (n = 0):\n"
              "  t_0 = 0,  T_0 = 90°C\n"
              "  f(t_0, T_0) = -0.05 * (90 - 20) = -0.05 * 70 = -3.5°C/min\n"
              "  T_1 = T(4) = T_0 + h * f(t_0, T_0)\n"
              "             = 90 + 4 * (-3.5) = 90 - 14.0 = 76.0°C\n\n"
              "Step 2: At t = 4 min to estimate T(8) (n = 1):\n"
              "  t_1 = 4,  T_1 = 76.0°C\n"
              "  f(t_1, T_1) = -0.05 * (76.0 - 20) = -0.05 * 56.0 = -2.8°C/min\n"
              "  T_2 = T(8) = T_1 + h * f(t_1, T_1)\n"
              "             = 76.0 + 4 * (-2.8) = 76.0 - 11.2 = 64.8°C\n\n"
              "Final Answer:\n"
              "    The estimated temperature of the object after 8 minutes is 64.8°C.")

    p = doc.add_paragraph()
    r = p.add_run("Python Program:")
    r.bold = True
    
    code_q4 = '''# ==============================================================================
# Problem 4: Application of Euler's Method - Newton's Law of Cooling
# dT/dt = -k * (T - Ta), k = 0.05 /min, Ta = 20 C, T(0) = 90 C, h = 4 min
# ==============================================================================

def newtons_cooling_euler(k=0.05, Ta=20.0, T0=90.0, h=4.0, t_end=8.0):
    t, T = 0.0, T0
    steps = int(round(t_end / h))
    
    print("Application of Euler's Method: Newton's Law of Cooling")
    print(f"Parameters: k = {k}/min, Ta = {Ta} C, T(0) = {T0} C, Step size h = {h} min")
    print("-" * 65)
    print(f"{'Step':<6}{'Time t (min)':<15}{'Current T (C)':<16}{'dT/dt (C/min)':<16}{'Next T (C)':<12}")
    print("-" * 65)
    
    for i in range(steps):
        rate = -k * (T - Ta)
        T_next = T + h * rate
        print(f"{i+1:<6}{t:<15.1f}{T:<16.2f}{rate:<16.2f}{T_next:<12.2f}")
        t += h
        T = T_next
        
    print("-" * 65)
    print(f"Final estimated temperature after {t_end:.0f} minutes: T({t_end:.0f}) = {T:.2f} C")

if __name__ == "__main__":
    newtons_cooling_euler()'''
    add_code_block(code_q4)

    p = doc.add_paragraph()
    r = p.add_run("OUTPUT:")
    r.bold = True

    out_q4 = '''Application of Euler's Method: Newton's Law of Cooling
Parameters: k = 0.05/min, Ta = 20.0 C, T(0) = 90.0 C, Step size h = 4.0 min
-----------------------------------------------------------------
Step  Time t (min)   Current T (C)   dT/dt (C/min)   Next T (C)  
-----------------------------------------------------------------
1     0.0            90.00           -3.50           76.00       
2     4.0            76.00           -2.80           64.80       
-----------------------------------------------------------------
Final estimated temperature after 8 minutes: T(8) = 64.80 C'''
    add_output_block(out_q4)

    # ------------------ PROBLEM 5 ------------------
    add_heading_styled("5. Problem - 5: Runge–Kutta Second-Order (RK2) Method", level=1)
    
    p = doc.add_paragraph()
    r = p.add_run("Problem Statement:\n")
    r.bold = True
    p.add_run("Using the second-order Runge–Kutta (RK2) method, solve the differential equation:\n"
              "    dy/dx = sin(x - y),\n"
              "given y(0) = 1. Compute y(0.3) using step size h = 0.1.")

    p = doc.add_paragraph()
    r = p.add_run("Manual Solution:")
    r.bold = True
    
    p = doc.add_paragraph()
    p.add_run("Given:\n"
              "    f(x, y) = sin(x - y)   (angles evaluated in radians)\n"
              "    Initial condition: x_0 = 0, y_0 = 1\n"
              "    Step size: h = 0.1\n\n"
              "Second-Order Runge–Kutta (RK2 / Heun's) Formulas:\n"
              "    k_1 = h * f(x_n, y_n)\n"
              "    k_2 = h * f(x_n + h, y_n + k_1)\n"
              "    y_(n+1) = y_n + (1/2) * (k_1 + k_2)\n\n"
              "• Step 1: Compute y(0.1) from x_0 = 0 to x_1 = 0.1 (y_0 = 1.0):\n"
              "  k_1 = 0.1 * sin(0 - 1) = 0.1 * sin(-1 rad) = 0.1 * (-0.841471) = -0.084147\n"
              "  x_0 + h = 0.1\n"
              "  y_0 + k_1 = 1 - 0.084147 = 0.915853\n"
              "  k_2 = 0.1 * sin(0.1 - 0.915853) = 0.1 * sin(-0.815853 rad) = 0.1 * (-0.728312) = -0.072831\n"
              "  Δy_0 = (1/2) * (-0.084147 + (-0.072831)) = (1/2) * (-0.156978) = -0.078489\n"
              "  y_1 = y(0.1) = 1.0 + (-0.078489) = 0.921511\n\n"
              "• Step 2: Compute y(0.2) from x_1 = 0.1 to x_2 = 0.2 (y_1 = 0.921511):\n"
              "  k_1 = 0.1 * sin(0.1 - 0.921511) = 0.1 * sin(-0.821511 rad) = 0.1 * (-0.732182) = -0.073218\n"
              "  x_1 + h = 0.2\n"
              "  y_1 + k_1 = 0.921511 - 0.073218 = 0.848293\n"
              "  k_2 = 0.1 * sin(0.2 - 0.848293) = 0.1 * sin(-0.648293 rad) = 0.1 * (-0.603830) = -0.060383\n"
              "  Δy_1 = (1/2) * (-0.073218 + (-0.060383)) = (1/2) * (-0.133601) = -0.066801\n"
              "  y_2 = y(0.2) = 0.921511 + (-0.066801) = 0.854710\n\n"
              "• Step 3: Compute y(0.3) from x_2 = 0.2 to x_3 = 0.3 (y_2 = 0.854710):\n"
              "  k_1 = 0.1 * sin(0.2 - 0.854710) = 0.1 * sin(-0.654710 rad) = 0.1 * (-0.608927) = -0.060893\n"
              "  x_2 + h = 0.3\n"
              "  y_2 + k_1 = 0.854710 - 0.060893 = 0.793817\n"
              "  k_2 = 0.1 * sin(0.3 - 0.793817) = 0.1 * sin(-0.493817 rad) = 0.1 * (-0.473993) = -0.047399\n"
              "  Δy_2 = (1/2) * (-0.060893 + (-0.047399)) = (1/2) * (-0.108292) = -0.054146\n"
              "  y_3 = y(0.3) = 0.854710 + (-0.054146) = 0.800564 ≈ 0.8006\n\n"
              "Final Results:\n"
              "    y(0.1) ≈ 0.9215\n"
              "    y(0.2) ≈ 0.8547\n"
              "    y(0.3) ≈ 0.8006")

    p = doc.add_paragraph()
    r = p.add_run("Python Program:")
    r.bold = True
    
    code_q5 = '''# ==============================================================================
# Problem 5: Runge-Kutta 2nd Order (RK2) Method
# ODE: dy/dx = sin(x - y), y(0) = 1, h = 0.1, Target: y(0.3)
# ==============================================================================
import math

def f(x, y):
    """Derivative function dy/dx = sin(x - y)"""
    return math.sin(x - y)

def rk2_heun(x0, y0, h, x_end):
    print("Runge-Kutta 2nd Order (RK2) Method")
    print(f"ODE: dy/dx = sin(x - y), y({x0}) = {y0}, step size h = {h}")
    print("-" * 65)
    print(f"{'Step':<6}{'x_n':<8}{'k1':<12}{'k2':<12}{'y_(n+1)':<12}")
    print("-" * 65)
    
    x, y = x0, y0
    steps = int(round((x_end - x0) / h))
    
    for i in range(steps):
        k1 = h * f(x, y)
        k2 = h * f(x + h, y + k1)
        y_next = y + 0.5 * (k1 + k2)
        x = round(x + h, 4)
        print(f"{i+1:<6}{x:<8.2f}{k1:<12.6f}{k2:<12.6f}{y_next:<12.6f}")
        y = y_next
        
    print("-" * 65)
    print(f"Final estimated y({x_end}) = {y:.4f}")

if __name__ == "__main__":
    rk2_heun(x0=0.0, y0=1.0, h=0.1, x_end=0.3)'''
    add_code_block(code_q5)

    p = doc.add_paragraph()
    r = p.add_run("OUTPUT:")
    r.bold = True

    out_q5 = '''Runge-Kutta 2nd Order (RK2) Method
ODE: dy/dx = sin(x - y), y(0.0) = 1.0, step size h = 0.1
-----------------------------------------------------------------
Step  x_n     k1          k2          y_(n+1)     
-----------------------------------------------------------------
1     0.10    -0.084147   -0.072831   0.921511    
2     0.20    -0.073218   -0.060383   0.854711    
3     0.30    -0.060893   -0.047399   0.800565    
-----------------------------------------------------------------
Final estimated y(0.3) = 0.8006'''
    add_output_block(out_q5)

    # ------------------ PROBLEM 6 ------------------
    add_heading_styled("6. Problem - 6: Application of RK2 Method: Salt Mixture Problem", level=1)
    
    p = doc.add_paragraph()
    r = p.add_run("Problem Statement:\n")
    r.bold = True
    p.add_run("A tank initially contains 80 liters of pure water. Brine containing 3 grams of salt per liter flows into "
              "the tank at a rate of 4 liters per minute, and the well-mixed solution flows out at the same rate.\n"
              "Let y(t) denote the amount of salt, in grams, in the tank at time t minutes. The rate of change of salt is given by:\n"
              "    dy/dt = 12 - y/20.\n"
              "Using the second-order Runge–Kutta method with step size h = 5 minutes, estimate the amount of salt in the tank "
              "after 15 minutes, given y(0) = 0.")

    p = doc.add_paragraph()
    r = p.add_run("Manual Solution:")
    r.bold = True
    
    p = doc.add_paragraph()
    p.add_run("Derivation & Model Setup:\n"
              "  • Inflow rate of salt: 4 L/min * 3 g/L = 12 g/min\n"
              "  • Volume remains constant: V = 80 L (inflow = outflow = 4 L/min)\n"
              "  • Outflow rate of salt: 4 L/min * (y / 80) g/L = y / 20 g/min\n"
              "  • Rate of change: dy/dt = 12 - y/20 = 12 - 0.05y\n"
              "  • Initial condition: t_0 = 0, y_0 = 0\n"
              "  • Step size: h = 5 minutes\n"
              "  • Target: y(15) after 3 steps (t = 5, 10, 15)\n\n"
              "RK2 (Heun's) Iterative Formulas:\n"
              "    k_1 = h * f(t_n, y_n)\n"
              "    k_2 = h * f(t_n + h, y_n + k_1)\n"
              "    y_(n+1) = y_n + (1/2) * (k_1 + k_2)\n\n"
              "• Step 1: From t = 0 to t = 5 min (t_0 = 0, y_0 = 0):\n"
              "  k_1 = 5 * (12 - 0.05 * 0) = 5 * 12 = 60.0000\n"
              "  y_0 + k_1 = 0 + 60 = 60\n"
              "  k_2 = 5 * (12 - 0.05 * 60) = 5 * (12 - 3) = 5 * 9 = 45.0000\n"
              "  y_1 = y(5) = y_0 + (1/2) * (60.0000 + 45.0000) = 0 + 52.5000 = 52.5000 g\n\n"
              "• Step 2: From t = 5 to t = 10 min (t_1 = 5, y_1 = 52.5):\n"
              "  k_1 = 5 * (12 - 0.05 * 52.5) = 5 * (12 - 2.625) = 5 * 9.375 = 46.8750\n"
              "  y_1 + k_1 = 52.5 + 46.875 = 99.375\n"
              "  k_2 = 5 * (12 - 0.05 * 99.375) = 5 * (12 - 4.96875) = 5 * 7.03125 = 35.15625\n"
              "  y_2 = y(10) = 52.5 + (1/2) * (46.8750 + 35.15625) = 52.5 + 41.015625 = 93.5156 g\n\n"
              "• Step 3: From t = 10 to t = 15 min (t_2 = 10, y_2 = 93.515625):\n"
              "  k_1 = 5 * (12 - 0.05 * 93.515625) = 5 * (12 - 4.675781) = 5 * 7.324219 = 36.6211\n"
              "  y_2 + k_1 = 93.515625 + 36.621094 = 130.136719\n"
              "  k_2 = 5 * (12 - 0.05 * 130.136719) = 5 * (12 - 6.506836) = 5 * 5.493164 = 27.4658\n"
              "  y_3 = y(15) = 93.515625 + (1/2) * (36.621094 + 27.465820) = 93.515625 + 32.043457 = 125.5591 g\n\n"
              "Final Answer:\n"
              "    The estimated amount of salt in the tank after 15 minutes is 125.5591 grams.\n\n"
              "Analytical Verification:\n"
              "    Exact ODE solution: y(t) = 240 * (1 - e^(-t / 20))\n"
              "    At t = 15: y(15) = 240 * (1 - e^(-0.75)) = 240 * (1 - 0.472367) ≈ 126.6320 grams\n"
              "    Relative numerical error is only ~0.85%, verifying excellent accuracy.")

    p = doc.add_paragraph()
    r = p.add_run("Python Program:")
    r.bold = True
    
    code_q6 = '''# ==============================================================================
# Problem 6: Application of RK2 - Salt Mixture Problem
# Tank ODE: dy/dt = 12 - y/20, y(0) = 0, h = 5 min, Target: y(15)
# ==============================================================================
import math

def dydt(t, y):
    """Rate of change of salt in the tank (g/min)"""
    return 12.0 - y / 20.0

def salt_mixture_rk2(h=5.0, t_end=15.0):
    t, y = 0.0, 0.0
    steps = int(round(t_end / h))
    
    print("Application of Runge-Kutta 2nd Order: Salt Mixture Problem")
    print(f"Inflow: 4 L/min @ 3 g/L = 12 g/min, Outflow: 4 L/min, Tank Volume: 80 L")
    print(f"Differential Equation: dy/dt = 12 - y/20, y(0) = 0, Step size h = {h} min")
    print("-" * 70)
    print(f"{'Step':<6}{'Time t (min)':<14}{'k1 (g)':<14}{'k2 (g)':<14}{'Salt y(t) (g)':<14}")
    print("-" * 70)
    
    for i in range(steps):
        k1 = h * dydt(t, y)
        k2 = h * dydt(t + h, y + k1)
        y_next = y + 0.5 * (k1 + k2)
        t += h
        print(f"{i+1:<6}{t:<14.1f}{k1:<14.4f}{k2:<14.4f}{y_next:<14.4f}")
        y = y_next
        
    print("-" * 70)
    print(f"Final estimated salt after {t_end:.0f} minutes: y({t_end:.0f}) = {y:.4f} grams")
    
    # Analytical solution for validation
    exact_salt = 240.0 * (1.0 - math.exp(-t_end / 20.0))
    print(f"Analytical exact solution: y_exact({t_end:.0f}) = {exact_salt:.4f} grams")
    print(f"Percentage Absolute Error: {abs(y - exact_salt) / exact_salt * 100:.2f}%")

if __name__ == "__main__":
    salt_mixture_rk2()'''
    add_code_block(code_q6)

    p = doc.add_paragraph()
    r = p.add_run("OUTPUT:")
    r.bold = True

    out_q6 = '''Application of Runge-Kutta 2nd Order: Salt Mixture Problem
Inflow: 4 L/min @ 3 g/L = 12 g/min, Outflow: 4 L/min, Tank Volume: 80 L
Differential Equation: dy/dt = 12 - y/20, y(0) = 0, Step size h = 5.0 min
----------------------------------------------------------------------
Step  Time t (min)  k1 (g)        k2 (g)        Salt y(t) (g) 
----------------------------------------------------------------------
1     5.0           60.0000       45.0000       52.5000       
2     10.0          46.8750       35.1562       93.5156       
3     15.0          36.6211       27.4658       125.5591      
----------------------------------------------------------------------
Final estimated salt after 15 minutes: y(15) = 125.5591 grams
Analytical exact solution: y_exact(15) = 126.6320 grams
Percentage Absolute Error: 0.85%'''
    add_output_block(out_q6)

    output_path = os.path.join(scratch_dir, "CS2807_Numerical_Methods_Activity_Report.docx")
    doc.save(output_path)
    print(f"Successfully generated DOCX at: {output_path}")

if __name__ == "__main__":
    create_report()
