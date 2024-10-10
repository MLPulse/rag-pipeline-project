import PyPDF2
import os

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + '\n'
    return text

if __name__ == "__main__":
    pdf_path = '../data/sample.pdf'
    text = extract_text_from_pdf(pdf_path)
    print(text)
