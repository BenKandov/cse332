import numpy as np
import pandas as pd
from sklearn import manifold
from scipy.stats import pearsonr

ran = np.random.RandomState(seed=3)
data = pd.read_csv("pokemon_processed_just_values.csv")

distance = lambda column1, column2: pearsonr(column1, column2)[0]
result = data.apply(lambda col1: data.apply(lambda col2: distance(col1,col2)))

mds = manifold.MDS(n_components=2, max_iter=300, eps=1e-9, random_state=ran,
                   dissimilarity="precomputed", n_jobs=1)

pos = mds.fit(result).embedding_


np.savetxt('correlation_mds.csv',pos,delimiter=',')
