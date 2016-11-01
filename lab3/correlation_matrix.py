import pandas as pd
import matplotlib.pyplot as plt

pokemon_df = pd.read_csv('pokemon_processed.csv')

pokemon_df.corr().to_csv("correlation_matrix.csv")

