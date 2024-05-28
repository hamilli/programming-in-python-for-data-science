import pandas as pd

# The data

hockey_players = pd.read_csv('data/canucks.csv')

# Select all the rows from column Salary only 
# Save it as player_cost 
# (Hint: you don't need loc here) 

player_cost = hockey_players[['Salary']]

# Display it

player_cost
