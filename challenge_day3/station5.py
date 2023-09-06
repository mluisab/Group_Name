import pandas as pd

df = pd.read_csv('teams_names.csv')
names = df["Name"].tolist()
teams = df['Team'].tolist()

def solution_station_5(station5_input): 
    try:
        index = names.index(station5_input)
        return int(teams[index])
    except ValueError:
        return int(0)



