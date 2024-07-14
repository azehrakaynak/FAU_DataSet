from pathlib import Path
from pdfminer.high_level import extract_text

def extract_pdf_text(pdf_path, txt_folder):
    txt_folder.mkdir(parents=True, exist_ok=True)
    txt_path = txt_folder / (pdf_path.stem + '.txt')

    try:
        text = extract_text(str(pdf_path))
        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(text.strip())
        print(f"Extracted text from {pdf_path.name} to {txt_path.name}")

    except Exception as e:
        print(f"Error extracting text from {pdf_path.name}: {e}")
        with open('error_log.txt', 'a', encoding='utf-8') as log_file:
            log_file.write(f"Error extracting text from {pdf_path.name}: {e}\n")

if __name__ == "__main__":
    pdf_folder = Path('data/pdfs')  # Folder contains PDF files
    txt_folder = Path('data/txts')  # Folder where TXT files will be saved

    # Extract text from downloaded PDF files
    for pdf_file in pdf_folder.glob('*.pdf'):
        extract_pdf_text(pdf_file, txt_folder)



