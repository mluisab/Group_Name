import pandas as pd

df = pd.read_csv('teams_names.csv')
names = df["Name"].tolist()
teams = df['Team'].tolist()

def solution_station_5(station5_input): 
    try:
        index = names.index(station5_input)
        return teams[index]
    except ValueError:
        return "Name not found"  

station5_input = "Isis"  
station5_output = solution_station_5(station5_input)
print(f"Team for {station5_input}: {station5_output}")