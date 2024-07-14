import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import os

nltk.download('punkt')

def chunk_txt(txt, max_toks=100):
    sents = sent_tokenize(txt)
    chks = []
    cur_chk = []
    cur_len = 0

    for sent in sents:
        toks = word_tokenize(sent)
        if cur_len + len(toks) > max_toks:
            chks.append(' '.join(cur_chk))
            cur_chk = toks
            cur_len = len(toks)
        else:
            cur_chk.extend(toks)
            cur_len += len(toks)

    if cur_chk:
        chks.append(' '.join(cur_chk))

    return chks

def proc_files(paths):
    for path in paths:
        with open(path, 'r', encoding='utf-8') as f:
            txt = f.read()

        chks = chunk_txt(txt)
        clean_txt = '\n'.join(chks)

        with open(path, 'w', encoding='utf-8') as f:
            f.write(clean_txt)
        
        print(f"Processed and updated {path}")

if __name__ == "__main__":
    paths = [
        r"C:\Users\DARSHI\Desktop\Step_Task\ext_txt\ebook_1.txt",
        r"C:\Users\DARSHI\Desktop\Step_Task\ext_txt\ebook_2.txt",
        r"C:\Users\DARSHI\Desktop\Step_Task\ext_txt\ebook_3.txt"
    ]
    proc_files(paths)
