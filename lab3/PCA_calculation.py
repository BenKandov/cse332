from sklearn.decomposition import PCA
import pandas as pd
import numpy as np

data = pd.read_csv("pokemon_processed_just_values.csv")

pca = PCA(n_components=2)

temp = pca.fit_transform(data)

print(temp)


np.savetxt('PCAd_Data.csv',temp,delimiter=',')
