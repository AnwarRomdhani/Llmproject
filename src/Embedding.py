from Import import pdf

from sentence_transformers import SentenceTransformer

model=SentenceTransformer('all-MiniLM-L6-v2')

text_chunks=[pdf[i:i:500] for i in range(0,len(pdf),500)]
embeds=model.encode(text_chunks)