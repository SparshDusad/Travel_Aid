from fpdf import FPDF

def generate_pdf(text, filename="itinerary.pdf"):
    pdf = FPDF()
    pdf.add_page()

    # Load a Unicode font (DejaVu or similar)
    pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)
    pdf.set_font("DejaVu", size=12)

    for line in text.split('\n'):
        pdf.multi_cell(0, 10, line)

    pdf.output(filename)
    return filename
