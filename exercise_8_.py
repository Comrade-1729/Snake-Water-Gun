import os
from pypdf import PdfMerger, PdfReader, PdfWriter

class PDFMergerHandler:
    def __init__(self):
        self.pdf_dict = {}
        self.selected_pdfs = []
        self.update_pdf_list()

    def update_pdf_list(self):
        ''' Updates the list of PDF files in the current directory '''
        self.pdf_dict.clear()
        pdf_files = [f for f in os.listdir() if f.endswith('.pdf')]
        for index, file in enumerate(pdf_files):
            self.pdf_dict[str(index+1)] = file

    def display_pdf_list(self):
        ''' Prints available PDF files for user selection '''
        print('Available PDF Files:')
        if not self.pdf_dict:
            print("No PDF files found.")
        else:
            for index, file in self.pdf_dict.items():
                print(f'{index}. {file}')

    def select_pdf(self, file_index):
        ''' Adds a selected PDF to the list of PDFs to be merged '''
        if file_index in self.pdf_dict:
            self.selected_pdfs.append(self.pdf_dict[file_index])
        else:
            print('File Not Found!')

    def merge_pdfs(self):
        ''' Merges the selected PDFs into a new PDF file '''
        if len(self.selected_pdfs) < 2:
            print('At least two PDF files are required to merge!')
            return
        try:
            merger = PdfMerger()
            for file in self.selected_pdfs:
                merger.append(file)
            output_filename = f'merged_{len(self.selected_pdfs)}.pdf'
            merger.write(output_filename)
            merger.close()
            print(f'Merged PDF files into {output_filename}')
        except Exception as e:
            print(f"Error during merging: {e}")
        finally:
            self.selected_pdfs.clear()  # Clear after merging

    def encrypt_pdf(self, file_index, password):
        ''' Encrypts a selected PDF with a password '''
        if file_index not in self.pdf_dict:
            print('File Not Found!')
            return
        try:
            reader = PdfReader(self.pdf_dict[file_index])
            writer = PdfWriter()
            for page in reader.pages:
                writer.add_page(page)
            writer.encrypt(password)
            output_filename = f"encrypted_{self.pdf_dict[file_index]}"
            with open(output_filename, 'wb') as f:
                writer.write(f)
            print(f'File {self.pdf_dict[file_index]} has been encrypted.')
        except Exception as e:
            print(f"Error during encryption: {e}")

    def decrypt_pdf(self, file_index, password):
        ''' Decrypts a selected PDF with a password '''
        if file_index not in self.pdf_dict:
            print('File Not Found!')
            return
        try:
            reader = PdfReader(self.pdf_dict[file_index])
            if reader.is_encrypted:
                reader.decrypt(password)
            writer = PdfWriter()
            for page in reader.pages:
                writer.add_page(page)
            output_filename = f"decrypted_{self.pdf_dict[file_index]}"
            with open(output_filename, 'wb') as f:
                writer.write(f)
            print(f'File {self.pdf_dict[file_index]} has been decrypted.')
        except Exception as e:
            print(f"Error during decryption: {e}")

# Initialize the handler
pdf_handler = PDFMergerHandler()

while True:
    print('\nOptions:')
    print('1. List PDF files')
    print('2. Select PDF for merging')
    print('3. Merge selected PDFs')
    print('4. Encrypt a PDF')
    print('5. Decrypt a PDF')
    print('6. Quit')

    choice = input('Enter your choice: ').strip().lower()

    if choice == '1':
        pdf_handler.display_pdf_list()

    elif choice == '2':
        pdf_handler.display_pdf_list()
        file_index = input('Enter PDF number to select for merging: ')
        pdf_handler.select_pdf(file_index)

    elif choice == '3':
        print('Merging selected PDFs...')
        pdf_handler.merge_pdfs()

    elif choice == '4':
        pdf_handler.display_pdf_list()
        file_index = input('Enter PDF number to encrypt: ')
        password = input('Enter encryption password: ')
        pdf_handler.encrypt_pdf(file_index, password)

    elif choice == '5':
        pdf_handler.display_pdf_list()
        file_index = input('Enter PDF number to decrypt: ')
        password = input('Enter decryption password: ')
        pdf_handler.decrypt_pdf(file_index, password)

    elif choice == '6' or choice == 'q':
        print("Exiting...")
        break

    else:
        print('Invalid choice. Please try again.')
