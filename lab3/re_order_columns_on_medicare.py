import pandas as pd

pokemon_df = pd.read_csv('pokemon.csv')



'''
0 - Normal
1 - Grass
2 - Fire
3 - Water
4 - Fighting
5 - Flying
6 - Poison
7 - Ground
8 - Rock
9 - Bug
10 - Ghost
11 - Electric
12 - Psychic
13 - Ice
14 - Dragon
15 - Dark
16 - Steel
17 - Fairy
'''

pokemon_df['Type 1'].replace('Normal', 0, inplace=True)
pokemon_df['Type 2'].replace('Normal', 0, inplace=True)

pokemon_df['Type 1'].replace('Grass', 1, inplace=True)
pokemon_df['Type 2'].replace('Grass', 1, inplace=True)

pokemon_df['Type 1'].replace('Fire', 2, inplace=True)
pokemon_df['Type 2'].replace('Fire', 2, inplace=True)

pokemon_df['Type 1'].replace('Water', 3, inplace=True)
pokemon_df['Type 2'].replace('Water', 3, inplace=True)

pokemon_df['Type 1'].replace('Fighting', 4, inplace=True)
pokemon_df['Type 2'].replace('Fighting', 4, inplace=True)

pokemon_df['Type 1'].replace('Flying', 5, inplace=True)
pokemon_df['Type 2'].replace('Flying', 5, inplace=True)

pokemon_df['Type 1'].replace('Poison', 6, inplace=True)
pokemon_df['Type 2'].replace('Poison', 6, inplace=True)

pokemon_df['Type 1'].replace('Ground', 7, inplace=True)
pokemon_df['Type 2'].replace('Ground', 7, inplace=True)

pokemon_df['Type 1'].replace('Rock', 8, inplace=True)
pokemon_df['Type 2'].replace('Rock', 8, inplace=True)

pokemon_df['Type 1'].replace('Bug', 9, inplace=True)
pokemon_df['Type 2'].replace('Bug', 9, inplace=True)

pokemon_df['Type 1'].replace('Ghost', 10, inplace=True)
pokemon_df['Type 2'].replace('Ghost', 10, inplace=True)

pokemon_df['Type 1'].replace('Electric', 11, inplace=True)
pokemon_df['Type 2'].replace('Electric', 11, inplace=True)

pokemon_df['Type 1'].replace('Psychic', 12, inplace=True)
pokemon_df['Type 2'].replace('Psychic', 12, inplace=True)

pokemon_df['Type 1'].replace('Ice', 13, inplace=True)
pokemon_df['Type 2'].replace('Ice', 13, inplace=True)

pokemon_df['Type 1'].replace('Dragon', 14, inplace=True)
pokemon_df['Type 2'].replace('Dragon', 14, inplace=True)

pokemon_df['Type 1'].replace('Dark', 15, inplace=True)
pokemon_df['Type 2'].replace('Dark', 15, inplace=True)

pokemon_df['Type 1'].replace('Steel', 16, inplace=True)
pokemon_df['Type 2'].replace('Steel', 16, inplace=True)

pokemon_df['Type 1'].replace('Fairy', 17, inplace=True)
pokemon_df['Type 2'].replace('Fairy', 17, inplace=True)

pokemon_df['Legendary'] = pokemon_df['Legendary'] *1


print (type(pokemon_df["Legendary"][0]))
pokemon_df.to_csv("pokemon_processed.csv")

