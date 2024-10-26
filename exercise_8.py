'''
    Merge the pdf files
'''
import os
from pypdf import PdfWriter, PdfReader

def merge_pdf1(folder_path):
    '''
        Function to merge PDF files entirely.
    '''
    merger = PdfWriter()
    files = [file for file in os.listdir(folder_path) if file.endswith('.pdf')]
    l = len(files)
    for file in files:
        full_path = os.path.join(folder_path, file)
        merger.append(full_path)  # Append the entire file
    with open(os.path.join(folder_path, "merged1.pdf"), "wb") as output_file:
        merger.write(output_file)
    print(f"Merged {l} files into 'merged1.pdf'")

def merge_pdf2(folder_path):
    '''
        Function to merge PDF files selectively.
    '''
    merger = PdfWriter()
    files = [file for file in os.listdir(folder_path) if file.endswith('.pdf')]
    l = len(files)

    for index, file in enumerate(files, start=1):
        full_path = os.path.join(folder_path, file)
        reader = PdfReader(full_path)  # Create a reader for the PDF

        if index < 2 :
            # Append the entire document for 1st PDF
            merger.append(full_path)
        elif index > 2 :
            # Append the first and 10th page from the 3rd PDF
            if len(reader.pages) >= 10:
                [merger.add_page(reader.pages[i]) for i in [0,9]]
        else:
            # Append the first 10 pages of the 2nd PDF
            [merger.add_page(reader.pages[pg]) for pg in range(min(10,len(reader.pages)))]

    with open(os.path.join(folder_path, "merged2.pdf"), "wb") as output_file:
        merger.write(output_file)
    print(f"Merged {l} files selectively into 'merged2.pdf'")

FOLDER_PATH = r'D:\CODE\Exercises\pdf_files'
merge_pdf1(FOLDER_PATH)
merge_pdf2(FOLDER_PATH)
