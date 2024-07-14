from ebooklib import epub

def extract_text(epub_file):
    book = epub.read_epub(epub_file)
    text = []
    for item in book.get_items():
        if isinstance(item, epub.EpubHtml):
            content = item.get_content().decode('utf-8')
            text.append(content)
    return '\n'.join(text)

epubs = [
    r'C:\Users\DARSHI\Desktop\Step_Task\data\epub_files\Stephen-King-The-Stand_-The-Complete-_-Uncut-Edition-Doubleday-_1990_.epub',
    r'C:\Users\DARSHI\Desktop\Step_Task\data\epub_files\Stephen King - Misery-Signet (1998).epub',
    r'C:\Users\DARSHI\Desktop\Step_Task\data\epub_files\Stephen King - It_ A Novel-Signet (2009).epub'
]

for epub_file in epubs:
    extracted_text = extract_text(epub_file)
    print(f"Text extracted from '{epub_file}':")
    print(extracted_text)
