from ebooklib import epub
from bs4 import BeautifulSoup
import os

def extract(epub_file):
    book = epub.read_epub(epub_file)
    text = []
    for item in book.get_items():
        if isinstance(item, epub.EpubHtml):
            content = item.get_content()
            decoded_content = content.decode('utf-8', errors='ignore')
            soup = BeautifulSoup(decoded_content, 'html.parser')
            cleaned_text = soup.get_text(separator='\n', strip=True)
            text.append(cleaned_text)
    return '\n'.join(text)

def new_file(text, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)

epubs = [
    r'C:\Users\DARSHI\Desktop\Step_Task\epub_files\Stephen-King-The-Stand_-The-Complete-_-Uncut-Edition-Doubleday-_1990_.epub',
    r'C:\Users\DARSHI\Desktop\Step_Task\epub_files\Stephen King - Misery-Signet (1998).epub',
    r'C:\Users\DARSHI\Desktop\Step_Task\epub_files\Stephen King - It_ A Novel-Signet (2009).epub'
]

output_dir = 'extracted_text'
os.makedirs(output_dir, exist_ok=True)

for i, epub_file in enumerate(epubs):
    extracted_text = extract(epub_file)
    text_file_path = os.path.join(output_dir, f'ebook_{i+1}.txt')
    new_file(extracted_text, text_file_path)
    print(f"Text extracted from '{epub_file}' and saved to '{text_file_path}'")
