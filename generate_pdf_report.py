import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image, Preformatted
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def generate_pdf():
    scratch_dir = r"C:\Users\chand\.gemini\antigravity\scratch"
    pdf_path = os.path.join(scratch_dir, "CS2807_Numerical_Methods_Activity_Report.pdf")
    logo_path = os.path.join(scratch_dir, "logo_0.png")

    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        rightMargin=54,
        leftMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        alignment=1, # Center
        textColor=colors.black
    )

    report_sub_style = ParagraphStyle(
        'CoverSub',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        alignment=1,
        textColor=colors.black
    )

    name_style = ParagraphStyle(
        'CoverName',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=20,
        alignment=1,
        textColor=colors.HexColor('#C00000')
    )

    reg_style = ParagraphStyle(
        'CoverReg',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        alignment=1,
        textColor=colors.black
    )

    course_style = ParagraphStyle(
        'CoverCourse',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=19,
        alignment=1,
        textColor=colors.black
    )

    body_center = ParagraphStyle(
        'CoverCenter',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        leading=16,
        alignment=1,
        textColor=colors.black
    )

    univ_style = ParagraphStyle(
        'CoverUniv',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        alignment=1,
        textColor=colors.black
    )

    date_style = ParagraphStyle(
        'CoverDate',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        alignment=1,
        textColor=colors.HexColor('#C00000')
    )

    h1_style = ParagraphStyle(
        'ProbHeading',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=colors.HexColor('#003366'),
        spaceBefore=12,
        spaceAfter=6
    )

    h2_style = ParagraphStyle(
        'SubHeading',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#1A5276'),
        spaceBefore=8,
        spaceAfter=4
    )

    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor('#222222')
    )

    code_pre_style = ParagraphStyle(
        'CodeStyle',
        parent=styles['Code'],
        fontName='Courier',
        fontSize=7.8,
        leading=10.2,
        textColor=colors.HexColor('#1C2833')
    )

    output_pre_style = ParagraphStyle(
        'OutputStyle',
        parent=styles['Code'],
        fontName='Courier',
        fontSize=8.0,
        leading=10.5,
        textColor=colors.HexColor('#0E6251')
    )

    elements = []

    # ------------------ COVER PAGE ------------------
    elements.append(Paragraph("CIE-3-Coding Based Activity", title_style))
    elements.append(Spacer(1, 10))
    elements.append(Paragraph("A PROJECT REPORT", report_sub_style))
    elements.append(Spacer(1, 15))
    elements.append(Paragraph("Submitted by", report_sub_style))
    elements.append(Spacer(1, 10))
    elements.append(Paragraph("KRISHNA H CHANDAWAR", name_style))
    elements.append(Spacer(1, 5))
    elements.append(Paragraph("Register No: 1RUA25BCA0052<br/>Section: Section A", reg_style))
    elements.append(Spacer(1, 15))
    elements.append(Paragraph("<i>as part of the Continuous Internal Evaluation<br/>for the course</i>", body_center))
    elements.append(Spacer(1, 10))
    elements.append(Paragraph("CS2807 Numerical Methods", course_style))
    elements.append(Spacer(1, 5))
    elements.append(Paragraph("Offered in<br/><b>Semester III</b><br/>of<br/><b>BCA (Hons)</b>", body_center))
    elements.append(Spacer(1, 15))

    if os.path.exists(logo_path):
        elements.append(Image(logo_path, width=2.4*inch, height=1.3*inch))
        elements.append(Spacer(1, 15))

    elements.append(Paragraph(
        "School of Computer Science and Engineering<br/>"
        "RV University<br/>"
        "RV Vidyaniketan, 8th Mile, Mysore Road, Bengaluru, Karnataka, India - 560059",
        univ_style
    ))
    elements.append(Spacer(1, 15))
    elements.append(Paragraph("NOVEMBER 2026", date_style))
    elements.append(PageBreak())

    # Helper for code/output boxes
    def make_box(text, style, bg_color, border_color):
        p = Preformatted(text, style)
        t = Table([[p]], colWidths=[6.8 * inch])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), bg_color),
            ('BOX', (0,0), (-1,-1), 1, border_color),
            ('PADDING', (0,0), (-1,-1), 6),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ]))
        return t

    # ------------------ PROBLEM 1 ------------------
    elements.append(Paragraph("1. Problem - 1: Gauss–Jacobi Iterative Method", h1_style))
    elements.append(Paragraph("<b>Problem Statement:</b><br/>Solve the following system of linear equations using the Gauss–Jacobi iterative method up to four decimal places:<br/>&nbsp;&nbsp;&nbsp;&nbsp;9x - y + 2z = 18<br/>&nbsp;&nbsp;&nbsp;&nbsp;2x + 8y - z = -5<br/>&nbsp;&nbsp;&nbsp;&nbsp;x - 2y + 10z = 21<br/>Use the initial guess x<sup>(0)</sup> = 0, y<sup>(0)</sup> = 0, z<sup>(0)</sup> = 0.", body_style))
    elements.append(Spacer(1, 6))
    
    sol1 = (
        "<b>Manual Solution:</b><br/>"
        "<b>Step 1: Check for Strictly Diagonal Dominance</b><br/>"
        "&bull; |9| = 9 > |-1| + |2| = 3 (True)<br/>"
        "&bull; |8| = 8 > |2| + |-1| = 3 (True)<br/>"
        "&bull; |10| = 10 > |1| + |-2| = 3 (True)<br/>"
        "Since the coefficient matrix is diagonally dominant, convergence is guaranteed.<br/><br/>"
        "<b>Step 2: Gauss–Jacobi Iteration Formulas</b><br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;x<sup>(k+1)</sup> = (18 + y<sup>(k)</sup> - 2z<sup>(k)</sup>) / 9<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;y<sup>(k+1)</sup> = (-5 - 2x<sup>(k)</sup> + z<sup>(k)</sup>) / 8<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;z<sup>(k+1)</sup> = (21 - x<sup>(k)</sup> + 2y<sup>(k)</sup>) / 10<br/><br/>"
        "<b>Step 3: Iteration Calculations</b> (with x<sup>(0)</sup>=0, y<sup>(0)</sup>=0, z<sup>(0)</sup>=0):<br/>"
        "&bull; <b>Iteration 1 (k=0):</b> x<sup>(1)</sup> = 18/9 = 2.0000, y<sup>(1)</sup> = -5/8 = -0.6250, z<sup>(1)</sup> = 21/10 = 2.1000<br/>"
        "&bull; <b>Iteration 2 (k=1):</b> x<sup>(2)</sup> = (18 - 0.6250 - 4.2000)/9 = 1.4639, y<sup>(2)</sup> = (-5 - 4 + 2.1)/8 = -0.8625, z<sup>(2)</sup> = (21 - 2 - 1.25)/10 = 1.7750<br/>"
        "&bull; <b>Iteration 3 (k=2):</b> x<sup>(3)</sup> = (18 - 0.8625 - 3.5500)/9 = 1.5097, y<sup>(3)</sup> = -0.7691, z<sup>(3)</sup> = 1.7811<br/>"
        "&bull; <b>Iteration 4 (k=3):</b> x<sup>(4)</sup> = 1.5187, y<sup>(4)</sup> = -0.7798, z<sup>(4)</sup> = 1.7952<br/>"
        "&bull; <b>Iteration 5 (k=4):</b> x<sup>(5)</sup> = 1.5144, y<sup>(5)</sup> = -0.7803, z<sup>(5)</sup> = 1.7922<br/>"
        "&bull; <b>Iteration 6 (k=5):</b> x<sup>(6)</sup> = 1.5150, y<sup>(6)</sup> = -0.7796, z<sup>(6)</sup> = 1.7925<br/>"
        "&bull; <b>Iteration 7 (k=6):</b> x<sup>(7)</sup> = 1.5150, y<sup>(7)</sup> = -0.7797, z<sup>(7)</sup> = 1.7926<br/>"
        "&bull; <b>Iteration 8 (k=7):</b> x<sup>(8)</sup> = 1.5150, y<sup>(8)</sup> = -0.7797, z<sup>(8)</sup> = 1.7926<br/><br/>"
        "<b>Final Solution:</b> x = 1.5150, y = -0.7797, z = 1.7926"
    )
    elements.append(Paragraph(sol1, body_style))
    elements.append(Spacer(1, 6))

    code1 = """# Gauss-Jacobi Iterative Method
def gauss_jacobi(tol=1e-4, max_iter=50):
    x, y, z = 0.0, 0.0, 0.0
    print(f"Iteration  0: x = {x:.4f}, y = {y:.4f}, z = {z:.4f}")
    for k in range(1, max_iter + 1):
        x_new = (18.0 + y - 2.0 * z) / 9.0
        y_new = (-5.0 - 2.0 * x + z) / 8.0
        z_new = (21.0 - x + 2.0 * y) / 10.0
        print(f"Iteration {k:2d}: x = {x_new:.4f}, y = {y_new:.4f}, z = {z_new:.4f}")
        if max(abs(x_new - x), abs(y_new - y), abs(z_new - z)) < tol:
            print(f"\\nConvergence achieved at iteration {k}!")
            print(f"Final Solution: x = {x_new:.4f}, y = {y_new:.4f}, z = {z_new:.4f}")
            break
        x, y, z = x_new, y_new, z_new

gauss_jacobi()"""
    elements.append(Paragraph("<b>Python Program:</b>", h2_style))
    elements.append(make_box(code1, code_pre_style, colors.HexColor('#F8F9FA'), colors.HexColor('#D5D8DC')))
    elements.append(Spacer(1, 6))

    out1 = """Iteration  0: x = 0.0000, y = 0.0000, z = 0.0000
Iteration  1: x = 2.0000, y = -0.6250, z = 2.1000
Iteration  2: x = 1.4639, y = -0.8625, z = 1.7750
Iteration  3: x = 1.5097, y = -0.7691, z = 1.7811
Iteration  4: x = 1.5187, y = -0.7798, z = 1.7952
Iteration  5: x = 1.5144, y = -0.7803, z = 1.7922
Iteration  6: x = 1.5150, y = -0.7796, z = 1.7925
Iteration  7: x = 1.5150, y = -0.7797, z = 1.7926
Iteration  8: x = 1.5150, y = -0.7797, z = 1.7926

Convergence achieved at iteration 8!
Final Solution: x = 1.5150, y = -0.7797, z = 1.7926"""
    elements.append(Paragraph("<b>OUTPUT:</b>", h2_style))
    elements.append(make_box(out1, output_pre_style, colors.HexColor('#EAF2F8'), colors.HexColor('#A9CCE3')))
    elements.append(PageBreak())

    # ------------------ PROBLEM 2 ------------------
    elements.append(Paragraph("2. Problem - 2: Gauss–Seidel Method", h1_style))
    elements.append(Paragraph("<b>Problem Statement:</b><br/>Solve the following system of linear equations using the Gauss–Seidel method up to four decimal places:<br/>&nbsp;&nbsp;&nbsp;&nbsp;5x + y - z = 10<br/>&nbsp;&nbsp;&nbsp;&nbsp;-x + 6y + 2z = -2<br/>&nbsp;&nbsp;&nbsp;&nbsp;2x - y + 7z = 9<br/>Take the initial guesses: x<sup>(0)</sup> = 0, y<sup>(0)</sup> = 0, z<sup>(0)</sup> = 0.", body_style))
    elements.append(Spacer(1, 6))

    sol2 = (
        "<b>Manual Solution:</b><br/>"
        "<b>Step 1: Check for Strictly Diagonal Dominance</b><br/>"
        "&bull; |5| = 5 > |1| + |-1| = 2 (True)<br/>"
        "&bull; |6| = 6 > |-1| + |2| = 3 (True)<br/>"
        "&bull; |7| = 7 > |2| + |-1| = 3 (True)<br/>"
        "Convergence is guaranteed.<br/><br/>"
        "<b>Step 2: Gauss–Seidel Iteration Formulas (Immediate Substitution)</b><br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;x<sup>(k+1)</sup> = (10 - y<sup>(k)</sup> + z<sup>(k)</sup>) / 5<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;y<sup>(k+1)</sup> = (-2 + x<sup>(k+1)</sup> - 2z<sup>(k)</sup>) / 6<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;z<sup>(k+1)</sup> = (9 - 2x<sup>(k+1)</sup> + y<sup>(k+1)</sup>) / 7<br/><br/>"
        "<b>Step 3: Iteration Calculations</b> (with x<sup>(0)</sup>=0, y<sup>(0)</sup>=0, z<sup>(0)</sup>=0):<br/>"
        "&bull; <b>Iteration 1 (k=0):</b><br/>"
        "&nbsp;&nbsp;x<sup>(1)</sup> = (10 - 0 + 0)/5 = 2.0000<br/>"
        "&nbsp;&nbsp;y<sup>(1)</sup> = (-2 + 2.0000 - 0)/6 = 0.0000<br/>"
        "&nbsp;&nbsp;z<sup>(1)</sup> = (9 - 2(2.0000) + 0)/7 = 5/7 ≈ 0.7143<br/>"
        "&bull; <b>Iteration 2 (k=1):</b><br/>"
        "&nbsp;&nbsp;x<sup>(2)</sup> = (10 - 0 + 0.7143)/5 ≈ 2.1429<br/>"
        "&nbsp;&nbsp;y<sup>(2)</sup> = (-2 + 2.1429 - 2(0.7143))/6 ≈ -0.2143<br/>"
        "&nbsp;&nbsp;z<sup>(2)</sup> = (9 - 2(2.1429) - 0.2143)/7 ≈ 0.6429<br/>"
        "&bull; <b>Iteration 3 (k=2):</b> x<sup>(3)</sup> = 2.1714, y<sup>(3)</sup> = -0.1857, z<sup>(3)</sup> = 0.6388<br/>"
        "&bull; <b>Iteration 4 (k=3):</b> x<sup>(4)</sup> = 2.1649, y<sup>(4)</sup> = -0.1854, z<sup>(4)</sup> = 0.6407<br/>"
        "&bull; <b>Iteration 5 (k=4):</b> x<sup>(5)</sup> = 2.1652, y<sup>(5)</sup> = -0.1860, z<sup>(5)</sup> = 0.6405<br/>"
        "&bull; <b>Iteration 6 (k=5):</b> x<sup>(6)</sup> = 2.1653, y<sup>(6)</sup> = -0.1860, z<sup>(6)</sup> = 0.6405<br/><br/>"
        "<b>Final Solution:</b> x = 2.1653, y = -0.1860, z = 0.6405"
    )
    elements.append(Paragraph(sol2, body_style))
    elements.append(Spacer(1, 6))

    code2 = """# Gauss-Seidel Iterative Method
def gauss_seidel(tol=1e-4, max_iter=50):
    x, y, z = 0.0, 0.0, 0.0
    print(f"Iteration  0: x = {x:.4f}, y = {y:.4f}, z = {z:.4f}")
    for k in range(1, max_iter + 1):
        x_old, y_old, z_old = x, y, z
        x = (10.0 - y + z) / 5.0
        y = (-2.0 + x - 2.0 * z) / 6.0
        z = (9.0 - 2.0 * x + y) / 7.0
        print(f"Iteration {k:2d}: x = {x:.4f}, y = {y:.4f}, z = {z:.4f}")
        if max(abs(x - x_old), abs(y - y_old), abs(z - z_old)) < tol:
            print(f"\\nConvergence achieved at iteration {k}!")
            print(f"Final Solution: x = {x:.4f}, y = {y:.4f}, z = {z:.4f}")
            break

gauss_seidel()"""
    elements.append(Paragraph("<b>Python Program:</b>", h2_style))
    elements.append(make_box(code2, code_pre_style, colors.HexColor('#F8F9FA'), colors.HexColor('#D5D8DC')))
    elements.append(Spacer(1, 6))

    out2 = """Iteration  0: x = 0.0000, y = 0.0000, z = 0.0000
Iteration  1: x = 2.0000, y = 0.0000, z = 0.7143
Iteration  2: x = 2.1429, y = -0.2143, z = 0.6429
Iteration  3: x = 2.1714, y = -0.1857, z = 0.6388
Iteration  4: x = 2.1649, y = -0.1854, z = 0.6407
Iteration  5: x = 2.1652, y = -0.1860, z = 0.6405
Iteration  6: x = 2.1653, y = -0.1860, z = 0.6405

Convergence achieved at iteration 6!
Final Solution: x = 2.1653, y = -0.1860, z = 0.6405"""
    elements.append(Paragraph("<b>OUTPUT:</b>", h2_style))
    elements.append(make_box(out2, output_pre_style, colors.HexColor('#EAF2F8'), colors.HexColor('#A9CCE3')))
    elements.append(PageBreak())

    # ------------------ PROBLEM 3 ------------------
    elements.append(Paragraph("3. Problem - 3: Euler’s Method", h1_style))
    elements.append(Paragraph("<b>Problem Statement:</b><br/>Using Euler’s method with step size h = 0.1, estimate y(0.3) for the differential equation:<br/>&nbsp;&nbsp;&nbsp;&nbsp;dy/dx = x + y<sup>2</sup>,<br/>given y(0) = 1. Compute y(0.1), y(0.2), and y(0.3).", body_style))
    elements.append(Spacer(1, 6))

    sol3 = (
        "<b>Manual Solution:</b><br/>"
        "Euler's formula: <b>y<sub>n+1</sub> = y<sub>n</sub> + h &middot; f(x<sub>n</sub>, y<sub>n</sub>)</b>, where f(x, y) = x + y<sup>2</sup>.<br/><br/>"
        "&bull; <b>Step 1 (n = 0):</b> x<sub>0</sub> = 0, y<sub>0</sub> = 1<br/>"
        "&nbsp;&nbsp;f(x<sub>0</sub>, y<sub>0</sub>) = 0 + (1)<sup>2</sup> = 1.0<br/>"
        "&nbsp;&nbsp;y<sub>1</sub> = y(0.1) = 1 + 0.1(1.0) = <b>1.1000</b><br/><br/>"
        "&bull; <b>Step 2 (n = 1):</b> x<sub>1</sub> = 0.1, y<sub>1</sub> = 1.1<br/>"
        "&nbsp;&nbsp;f(x<sub>1</sub>, y<sub>1</sub>) = 0.1 + (1.1)<sup>2</sup> = 0.1 + 1.21 = 1.3100<br/>"
        "&nbsp;&nbsp;y<sub>2</sub> = y(0.2) = 1.1 + 0.1(1.3100) = <b>1.2310</b><br/><br/>"
        "&bull; <b>Step 3 (n = 2):</b> x<sub>2</sub> = 0.2, y<sub>2</sub> = 1.231<br/>"
        "&nbsp;&nbsp;f(x<sub>2</sub>, y<sub>2</sub>) = 0.2 + (1.231)<sup>2</sup> = 0.2 + 1.515361 = 1.715361<br/>"
        "&nbsp;&nbsp;y<sub>3</sub> = y(0.3) = 1.231 + 0.1(1.715361) = 1.231 + 0.171536 = <b>1.4025</b><br/><br/>"
        "<b>Final Values:</b> y(0.1) = 1.1000, y(0.2) = 1.2310, y(0.3) &approx; 1.4025"
    )
    elements.append(Paragraph(sol3, body_style))
    elements.append(Spacer(1, 6))

    code3 = """# Euler's Method for ODE
def f(x, y):
    return x + y**2

def euler(x0=0.0, y0=1.0, h=0.1, x_end=0.3):
    steps = int(round((x_end - x0) / h))
    x, y = x0, y0
    print(f"{'Step':<6}{'x_n':<10}{'y_n':<12}{'f(x, y)':<15}{'y_(n+1)':<12}")
    print("-" * 55)
    for i in range(steps):
        slope = f(x, y)
        y_next = y + h * slope
        print(f"{i+1:<6}{x:<10.2f}{y:<12.4f}{slope:<15.6f}{y_next:<12.4f}")
        x = round(x + h, 4)
        y = y_next
    print(f"\\nFinal estimated y({x_end}) = {y:.4f}")

euler()"""
    elements.append(Paragraph("<b>Python Program:</b>", h2_style))
    elements.append(make_box(code3, code_pre_style, colors.HexColor('#F8F9FA'), colors.HexColor('#D5D8DC')))
    elements.append(Spacer(1, 6))

    out3 = """Step  x_n       y_n         f(x, y)        y_(n+1)     
-------------------------------------------------------
1     0.00      1.0000      1.000000       1.1000      
2     0.10      1.1000      1.310000       1.2310      
3     0.20      1.2310      1.715361       1.4025      

Final estimated y(0.3) = 1.4025"""
    elements.append(Paragraph("<b>OUTPUT:</b>", h2_style))
    elements.append(make_box(out3, output_pre_style, colors.HexColor('#EAF2F8'), colors.HexColor('#A9CCE3')))
    elements.append(PageBreak())

    # ------------------ PROBLEM 4 ------------------
    elements.append(Paragraph("4. Problem - 4: Application of Euler’s Method: Newton’s Law of Cooling", h1_style))
    elements.append(Paragraph("<b>Problem Statement:</b><br/>The temperature T of a hot object placed in a room satisfies Newton’s Law of Cooling:<br/>&nbsp;&nbsp;&nbsp;&nbsp;dT/dt = -k(T - T<sub>a</sub>),<br/>where k = 0.05 per minute and the ambient temperature is T<sub>a</sub> = 20&deg;C. If the initial temperature of the object is T(0) = 90&deg;C, use Euler’s method with step size h = 4 minutes to estimate the temperature after 8 minutes.", body_style))
    elements.append(Spacer(1, 6))

    sol4 = (
        "<b>Manual Solution:</b><br/>"
        "Given: dT/dt = -0.05(T - 20), T(0) = 90&deg;C, h = 4 min.<br/>"
        "Euler update: <b>T<sub>n+1</sub> = T<sub>n</sub> + h &middot; f(t<sub>n</sub>, T<sub>n</sub>)</b><br/><br/>"
        "&bull; <b>Step 1 (t = 0 to 4 min):</b><br/>"
        "&nbsp;&nbsp;t<sub>0</sub> = 0, T<sub>0</sub> = 90&deg;C<br/>"
        "&nbsp;&nbsp;f(0, 90) = -0.05(90 - 20) = -0.05(70) = -3.5&deg;C/min<br/>"
        "&nbsp;&nbsp;T<sub>1</sub> = T(4) = 90 + 4(-3.5) = 90 - 14.0 = <b>76.0&deg;C</b><br/><br/>"
        "&bull; <b>Step 2 (t = 4 to 8 min):</b><br/>"
        "&nbsp;&nbsp;t<sub>1</sub> = 4 min, T<sub>1</sub> = 76.0&deg;C<br/>"
        "&nbsp;&nbsp;f(4, 76) = -0.05(76 - 20) = -0.05(56) = -2.8&deg;C/min<br/>"
        "&nbsp;&nbsp;T<sub>2</sub> = T(8) = 76.0 + 4(-2.8) = 76.0 - 11.2 = <b>64.8&deg;C</b><br/><br/>"
        "<b>Final Answer:</b> Temperature after 8 minutes = <b>64.8&deg;C</b>"
    )
    elements.append(Paragraph(sol4, body_style))
    elements.append(Spacer(1, 6))

    code4 = """# Newton's Law of Cooling using Euler's Method
def newtons_cooling_euler(k=0.05, Ta=20.0, T0=90.0, h=4.0, t_end=8.0):
    t, T = 0.0, T0
    steps = int(round(t_end / h))
    print(f"{'Step':<6}{'Time t (min)':<15}{'Current T (C)':<16}{'dT/dt (C/min)':<16}{'Next T (C)':<12}")
    print("-" * 65)
    for i in range(steps):
        rate = -k * (T - Ta)
        T_next = T + h * rate
        print(f"{i+1:<6}{t:<15.1f}{T:<16.2f}{rate:<16.2f}{T_next:<12.2f}")
        t += h
        T = T_next
    print(f"\\nEstimated temperature after {t_end:.0f} minutes: T({t_end:.0f}) = {T:.2f} C")

newtons_cooling_euler()"""
    elements.append(Paragraph("<b>Python Program:</b>", h2_style))
    elements.append(make_box(code4, code_pre_style, colors.HexColor('#F8F9FA'), colors.HexColor('#D5D8DC')))
    elements.append(Spacer(1, 6))

    out4 = """Step  Time t (min)   Current T (C)   dT/dt (C/min)   Next T (C)  
-----------------------------------------------------------------
1     0.0            90.00           -3.50           76.00       
2     4.0            76.00           -2.80           64.80       

Estimated temperature after 8 minutes: T(8) = 64.80 C"""
    elements.append(Paragraph("<b>OUTPUT:</b>", h2_style))
    elements.append(make_box(out4, output_pre_style, colors.HexColor('#EAF2F8'), colors.HexColor('#A9CCE3')))
    elements.append(PageBreak())

    # ------------------ PROBLEM 5 ------------------
    elements.append(Paragraph("5. Problem - 5: Runge–Kutta Second-Order (RK2) Method", h1_style))
    elements.append(Paragraph("<b>Problem Statement:</b><br/>Using the second-order Runge–Kutta (RK2) method, solve the differential equation:<br/>&nbsp;&nbsp;&nbsp;&nbsp;dy/dx = sin(x - y),<br/>given y(0) = 1. Compute y(0.3) using step size h = 0.1.", body_style))
    elements.append(Spacer(1, 6))

    sol5 = (
        "<b>Manual Solution:</b><br/>"
        "RK2 (Heun's) Formulas:<br/>"
        "&nbsp;&nbsp;k<sub>1</sub> = h &middot; f(x<sub>n</sub>, y<sub>n</sub>)<br/>"
        "&nbsp;&nbsp;k<sub>2</sub> = h &middot; f(x<sub>n</sub> + h, y<sub>n</sub> + k<sub>1</sub>)<br/>"
        "&nbsp;&nbsp;y<sub>n+1</sub> = y<sub>n</sub> + &frac12;(k<sub>1</sub> + k<sub>2</sub>)<br/><br/>"
        "&bull; <b>Step 1 (x = 0 to 0.1):</b> x<sub>0</sub> = 0, y<sub>0</sub> = 1<br/>"
        "&nbsp;&nbsp;k<sub>1</sub> = 0.1 &middot; sin(-1 rad) = 0.1(-0.841471) = -0.084147<br/>"
        "&nbsp;&nbsp;y<sub>0</sub> + k<sub>1</sub> = 0.915853; k<sub>2</sub> = 0.1 &middot; sin(0.1 - 0.915853) = -0.072831<br/>"
        "&nbsp;&nbsp;&Delta;y<sub>0</sub> = &frac12;(-0.084147 - 0.072831) = -0.078489<br/>"
        "&nbsp;&nbsp;y<sub>1</sub> = y(0.1) = 1 - 0.078489 = <b>0.921511</b><br/><br/>"
        "&bull; <b>Step 2 (x = 0.1 to 0.2):</b> x<sub>1</sub> = 0.1, y<sub>1</sub> = 0.921511<br/>"
        "&nbsp;&nbsp;k<sub>1</sub> = 0.1 &middot; sin(0.1 - 0.921511) = -0.073218<br/>"
        "&nbsp;&nbsp;y<sub>1</sub> + k<sub>1</sub> = 0.848293; k<sub>2</sub> = 0.1 &middot; sin(0.2 - 0.848293) = -0.060383<br/>"
        "&nbsp;&nbsp;&Delta;y<sub>1</sub> = &frac12;(-0.073218 - 0.060383) = -0.066801<br/>"
        "&nbsp;&nbsp;y<sub>2</sub> = y(0.2) = 0.921511 - 0.066801 = <b>0.854710</b><br/><br/>"
        "&bull; <b>Step 3 (x = 0.2 to 0.3):</b> x<sub>2</sub> = 0.2, y<sub>2</sub> = 0.854710<br/>"
        "&nbsp;&nbsp;k<sub>1</sub> = 0.1 &middot; sin(0.2 - 0.854710) = -0.060893<br/>"
        "&nbsp;&nbsp;y<sub>2</sub> + k<sub>1</sub> = 0.793817; k<sub>2</sub> = 0.1 &middot; sin(0.3 - 0.793817) = -0.047399<br/>"
        "&nbsp;&nbsp;&Delta;y<sub>2</sub> = &frac12;(-0.060893 - 0.047399) = -0.054146<br/>"
        "&nbsp;&nbsp;y<sub>3</sub> = y(0.3) = 0.854710 - 0.054146 = <b>0.800564 &approx; 0.8006</b><br/><br/>"
        "<b>Final Result:</b> y(0.3) &approx; <b>0.8006</b>"
    )
    elements.append(Paragraph(sol5, body_style))
    elements.append(Spacer(1, 6))

    code5 = """# Runge-Kutta 2nd Order (RK2) Method
import math

def f(x, y):
    return math.sin(x - y)

def rk2(x0=0.0, y0=1.0, h=0.1, x_end=0.3):
    x, y = x0, y0
    steps = int(round((x_end - x0) / h))
    print(f"{'Step':<6}{'x_n':<8}{'k1':<12}{'k2':<12}{'y_(n+1)':<12}")
    print("-" * 55)
    for i in range(steps):
        k1 = h * f(x, y)
        k2 = h * f(x + h, y + k1)
        y_next = y + 0.5 * (k1 + k2)
        x = round(x + h, 4)
        print(f"{i+1:<6}{x:<8.2f}{k1:<12.6f}{k2:<12.6f}{y_next:<12.6f}")
        y = y_next
    print(f"\\nFinal estimated y({x_end}) = {y:.4f}")

rk2()"""
    elements.append(Paragraph("<b>Python Program:</b>", h2_style))
    elements.append(make_box(code5, code_pre_style, colors.HexColor('#F8F9FA'), colors.HexColor('#D5D8DC')))
    elements.append(Spacer(1, 6))

    out5 = """Step  x_n     k1          k2          y_(n+1)     
-------------------------------------------------------
1     0.10    -0.084147   -0.072831   0.921511    
2     0.20    -0.073218   -0.060383   0.854711    
3     0.30    -0.060893   -0.047399   0.800565    

Final estimated y(0.3) = 0.8006"""
    elements.append(Paragraph("<b>OUTPUT:</b>", h2_style))
    elements.append(make_box(out5, output_pre_style, colors.HexColor('#EAF2F8'), colors.HexColor('#A9CCE3')))
    elements.append(PageBreak())

    # ------------------ PROBLEM 6 ------------------
    elements.append(Paragraph("6. Problem - 6: Application of RK2 Method: Salt Mixture Problem", h1_style))
    elements.append(Paragraph("<b>Problem Statement:</b><br/>A tank initially contains 80 liters of pure water. Brine containing 3 grams of salt per liter flows into the tank at a rate of 4 liters per minute, and the well-mixed solution flows out at the same rate. Let y(t) denote the amount of salt, in grams, in the tank at time t minutes. The rate of change of salt is given by:<br/>&nbsp;&nbsp;&nbsp;&nbsp;dy/dt = 12 - y/20.<br/>Using the second-order Runge–Kutta method with step size h = 5 minutes, estimate the amount of salt in the tank after 15 minutes, given y(0) = 0.", body_style))
    elements.append(Spacer(1, 6))

    sol6 = (
        "<b>Manual Solution:</b><br/>"
        "Model: dy/dt = 12 - 0.05y, y(0) = 0, h = 5 min.<br/>"
        "RK2 formula: y<sub>n+1</sub> = y<sub>n</sub> + &frac12;(k<sub>1</sub> + k<sub>2</sub>)<br/><br/>"
        "&bull; <b>Step 1 (t = 0 to 5 min):</b> t<sub>0</sub> = 0, y<sub>0</sub> = 0<br/>"
        "&nbsp;&nbsp;k<sub>1</sub> = 5(12 - 0) = 60.0000<br/>"
        "&nbsp;&nbsp;k<sub>2</sub> = 5(12 - 0.05(60)) = 5(9) = 45.0000<br/>"
        "&nbsp;&nbsp;y<sub>1</sub> = y(5) = 0 + &frac12;(60 + 45) = <b>52.5000 g</b><br/><br/>"
        "&bull; <b>Step 2 (t = 5 to 10 min):</b> t<sub>1</sub> = 5, y<sub>1</sub> = 52.5<br/>"
        "&nbsp;&nbsp;k<sub>1</sub> = 5(12 - 0.05(52.5)) = 5(9.375) = 46.8750<br/>"
        "&nbsp;&nbsp;y<sub>1</sub> + k<sub>1</sub> = 99.375; k<sub>2</sub> = 5(12 - 0.05(99.375)) = 35.1562<br/>"
        "&nbsp;&nbsp;y<sub>2</sub> = y(10) = 52.5 + &frac12;(46.8750 + 35.1562) = <b>93.5156 g</b><br/><br/>"
        "&bull; <b>Step 3 (t = 10 to 15 min):</b> t<sub>2</sub> = 10, y<sub>2</sub> = 93.515625<br/>"
        "&nbsp;&nbsp;k<sub>1</sub> = 5(12 - 0.05(93.515625)) = 36.6211<br/>"
        "&nbsp;&nbsp;y<sub>2</sub> + k<sub>1</sub> = 130.1367; k<sub>2</sub> = 5(12 - 0.05(130.1367)) = 27.4658<br/>"
        "&nbsp;&nbsp;y<sub>3</sub> = y(15) = 93.515625 + &frac12;(36.6211 + 27.4658) = <b>125.5591 g</b><br/><br/>"
        "<b>Final Answer:</b> Amount of salt after 15 minutes = <b>125.5591 grams</b><br/>"
        "<i>(Exact analytical solution: y(15) = 240(1 - e<sup>-0.75</sup>) &approx; 126.6320 g, relative error &approx; 0.85%).</i>"
    )
    elements.append(Paragraph(sol6, body_style))
    elements.append(Spacer(1, 6))

    code6 = """# Application of RK2 - Salt Mixture Problem
import math

def dydt(t, y):
    return 12.0 - y / 20.0

def salt_mixture(h=5.0, t_end=15.0):
    t, y = 0.0, 0.0
    steps = int(round(t_end / h))
    print(f"{'Step':<6}{'Time t (min)':<14}{'k1 (g)':<14}{'k2 (g)':<14}{'Salt y(t) (g)':<14}")
    print("-" * 65)
    for i in range(steps):
        k1 = h * dydt(t, y)
        k2 = h * dydt(t + h, y + k1)
        y_next = y + 0.5 * (k1 + k2)
        t += h
        print(f"{i+1:<6}{t:<14.1f}{k1:<14.4f}{k2:<14.4f}{y_next:<14.4f}")
        y = y_next
    print(f"\\nEstimated salt after {t_end:.0f} minutes: y({t_end:.0f}) = {y:.4f} grams")
    exact = 240.0 * (1.0 - math.exp(-t_end / 20.0))
    print(f"Exact analytical value: y_exact = {exact:.4f} grams")

salt_mixture()"""
    elements.append(Paragraph("<b>Python Program:</b>", h2_style))
    elements.append(make_box(code6, code_pre_style, colors.HexColor('#F8F9FA'), colors.HexColor('#D5D8DC')))
    elements.append(Spacer(1, 6))

    out6 = """Step  Time t (min)  k1 (g)        k2 (g)        Salt y(t) (g) 
-----------------------------------------------------------------
1     5.0           60.0000       45.0000       52.5000       
2     10.0          46.8750       35.1562       93.5156       
3     15.0          36.6211       27.4658       125.5591      

Estimated salt after 15 minutes: y(15) = 125.5591 grams
Exact analytical value: y_exact = 126.6320 grams"""
    elements.append(Paragraph("<b>OUTPUT:</b>", h2_style))
    elements.append(make_box(out6, output_pre_style, colors.HexColor('#EAF2F8'), colors.HexColor('#A9CCE3')))

    doc.build(elements)
    print(f"Successfully generated PDF at: {pdf_path}")

if __name__ == "__main__":
    generate_pdf()
