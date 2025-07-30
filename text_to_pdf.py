from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4 
import os

def txt_to_pdf(input_path, output_path=None):
    if not os.path.exists(input_path):
        print("❌ Text file not found!")
        return

    # Set output file name
    if output_path is None:
        output_path = os.path.splitext(input_path)[0] + '.pdf'

    # Read text file
    with open(input_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Create a PDF canvas
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4
    x = 40
    y = height - 40
    line_height = 15

    # Add each line to the PDF
    for line in lines:
        if y < 40:  # Start a new page if space is less
            c.showPage()
            y = height - 40
        c.drawString(x, y, line.strip())
        y -= line_height

    c.save()
    print(f"✅ PDF saved as: {output_path}")

# === Example Usage ===
if __name__ == "__main__":
    input_file = input("Enter path to your text file: ")
    txt_to_pdf(input_file)
