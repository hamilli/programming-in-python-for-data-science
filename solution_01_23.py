import pandas as pd

# The data

hockey_players = pd.read_csv('data/canucks.csv')
hockey_players

# Slice the rows and columns 
# Save the new dataframe as injured_players

injured_players = hockey_players.iloc[[16, 4, 21, 1], [0, 8, 7, 9]]

# Display it

injured_players 
