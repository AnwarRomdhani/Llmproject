from PyPDF2 import PdfReader

def get_pdf_text(pdf_path):
    """Retreive the pdf and open it"""
    reader=PdfReader(pdf_path)
    text=""
    for page in reader.pages:
        text += page.extract_text()
    return text

pdf_path="src/docs/Cs2_pro_guide.pdf"
pdf=get_pdf_text(pdf_path)
print(pdf)