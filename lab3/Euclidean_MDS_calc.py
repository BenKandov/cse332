import numpy as np
import pandas as pd
from sklearn import manifold
from sklearn.metrics import euclidean_distances

ran = np.random.RandomState(seed=3)
data = pd.read_csv("pokemon_processed_just_values.csv")

similarities = euclidean_distances(data)

mds = manifold.MDS(n_components=2, max_iter=300, eps=1e-9,random_state=ran,
                   dissimilarity="precomputed",n_jobs=1)

pos = mds.fit(similarities).embedding_
np.savetxt('foo.csv',pos,delimiter=',')
print(pos)