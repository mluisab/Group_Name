import pandas as pd

df = pd.read_csv('teams_names.csv')
names = df["Name"].tolist()
teams = df['Team'].tolist()
#def solution_station_5(): 

