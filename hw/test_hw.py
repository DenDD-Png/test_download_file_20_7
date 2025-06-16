import os
import zipfile
import PyPDF2
# Создаем папку "ресурсы", если её нет
os.makedirs('ресурсы', exist_ok=True)

def create_sample_files():
    # PDF файл
    with open('sample.pdf', 'wb') as f:
        pdf_writer = PyPDF2.PdfWriter()
        pdf_writer.add_blank_page(width=72, height=72)
        pdf_writer.write(f)