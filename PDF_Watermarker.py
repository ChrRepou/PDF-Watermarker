from PyPDF2 import PdfWriter, PdfReader
from pathlib import Path
import sys

def pdf_watermarker():
    if len(sys.argv) > 2:
        try:
            pdf_file = Path(sys.argv[1])
            watermark_file = Path(sys.argv[2])

            reader = PdfReader(watermark_file)
            watermark = reader.pages[0]
            writer = PdfWriter()

            reader = PdfReader(pdf_file)
            page_indices = list(range(0, len(reader.pages)))
            for index in page_indices:
                content_page = reader.pages[index]
                mediabox = content_page.mediabox
                content_page.merge_page(watermark)
                content_page.mediabox = mediabox
                writer.add_page(content_page)
            with open(pdf_file, "wb") as output_file:
                writer.write(output_file)
            print(f'The watermark has been written to {pdf_file} successfully.')
        except Exception as e:
            print(e)
    else:
        print('You should execute the script as: PDF_Watermarker.py <your_file.pdf> <watermark_file.pdf>')

if __name__ == '__main__':
    pdf_watermarker()