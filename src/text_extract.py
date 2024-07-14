from ebooklib import epub
from bs4 import BeautifulSoup
import os

def ext(epub_fp):
    bk = epub.read_epub(epub_fp)
    txt = []
    for itm in bk.get_items():
        if isinstance(itm, epub.EpubHtml):
            cnt = itm.get_content()
            dec_cnt = cnt.decode('utf-8', errors='ignore')
            soup = BeautifulSoup(dec_cnt, 'html.parser')
            clean_txt = soup.get_text(separator='\n', strip=True)
            txt.append(clean_txt)
    return '\n'.join(txt)

def save_txt(txt, fp):
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(txt)

epubs = [
    r'C:\Users\DARSHI\Desktop\Step_Task\epub_files\Stephen-King-The-Stand_-The-Complete-_-Uncut-Edition-Doubleday-_1990_.epub',
    r'C:\Users\DARSHI\Desktop\Step_Task\epub_files\Stephen King - Misery-Signet (1998).epub',
    r'C:\Users\DARSHI\Desktop\Step_Task\epub_files\Stephen King - It_ A Novel-Signet (2009).epub'
]

os.makedirs('ext_txt', exist_ok=True)

for i, epub_fp in enumerate(epubs):
    txt = ext(epub_fp)
    txt_fp = os.path.join('ext_txt', f'ebook_{i+1}.txt')
    save_txt(txt, txt_fp)
    print(f"Txt extracted from '{epub_fp}' and saved to '{txt_fp}'")
