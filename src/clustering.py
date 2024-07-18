from sklearn.mixture import GaussianMixture
import numpy as np

files = [
    'ext_txt/ebook_1.npy',
    'ext_txt/ebook_2.npy',
    'ext_txt/ebook_3.npy'
]

embeddings = []
for f in files:
    emb = np.load(f)
    embeddings.append(emb)

cluster_emb = np.vstack(embeddings)

gmm = GaussianMixture(n_components=10, covariance_type='tied')
gmm.fit(cluster_emb)
cluster_labels = gmm.predict(cluster_emb)

np.save('clusters.npy', cluster_labels)
