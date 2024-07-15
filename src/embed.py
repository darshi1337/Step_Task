from sentence_transformers import SentenceTransformer
import numpy as np
import os

def emb(chunks, mdl_name='paraphrase-MiniLM-L6-v2'):
    mdl = SentenceTransformer(mdl_name)
    embs = mdl.encode(chunks, show_progress_bar=True)
    return embs

def save_embs(embs, path):
    np.save(path, embs)

chks = []

for i in range(3):
    chk_path = f'ext_txt/ebook_{i+1}.txt'
    with open(chk_path, 'r', encoding='utf-8') as f:
        chunks = f.readlines()
        chunks = [chunk.strip() for chunk in chunks]
        chks.append(chunks)

for i, chunks in enumerate(chks):
    embs = emb(chunks)
    emb_path = os.path.join('ext_txt', f'ebook_{i+1}.npy')
    save_embs(embs, emb_path)
    print(f"Embeddings saved to '{emb_path}'")
