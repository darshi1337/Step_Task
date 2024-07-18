import numpy as np
from transformers import pipeline

summarizer = pipeline("summarization", model="allenai/llama-3-tulu-2-8b", device=0)

def summarize(embeddings):
    text = "\n".join(map(str, embeddings))
    
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)[0]['summary_text']
    
    return summary

embeddings = np.load('clusters.npy')
summary = summarize(embeddings)

print("Summary:")
print(summary)
