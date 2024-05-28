import pandas as pd

# Given dataframes

canucks = pd.read_csv('data/canucks.csv')
pokemon = pd.read_csv('data/pokemon.csv')
lego_themes = pd.read_csv('data/lego-themes.csv')
lego_inventory = pd.read_csv('data/lego_inventories.csv')

dataframes = [canucks, pokemon, lego_themes, lego_inventory]

# Of the 4 dataframes, how many of the have more than 1000 rows? 

count = 0
for data in dataframes:
    if data.shape[0] >1000:
        count += 1

# Display the value of count

count
