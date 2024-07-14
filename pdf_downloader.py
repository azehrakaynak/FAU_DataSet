import requests
from bs4 import BeautifulSoup
from pathlib import Path

def download_pdfs(base_url, pdf_folder):
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a', href=True)

    pdf_folder.mkdir(parents=True, exist_ok=True)

    for link in links:
        if link['href'].endswith('.pdf'):
            pdf_url = link['href'] if link['href'].startswith('http') else base_url + link['href']
            pdf_response = requests.get(pdf_url)
            pdf_name = pdf_url.split('/')[-1]
            pdf_path = pdf_folder / pdf_name

            with open(pdf_path, 'wb') as pdf_file:
                pdf_file.write(pdf_response.content)
            print(f"Downloaded: {pdf_name}")

if __name__ == "__main__":
    base_url = 'https://www.wiso.rw.fau.de/studium/im-studium/modulhandbuecher/#collapse_0'  # URL where PDF files are located
    pdf_folder = Path('data/pdfs')
    download_pdfs(base_url, pdf_folder)
