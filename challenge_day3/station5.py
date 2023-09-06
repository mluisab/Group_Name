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

station5_input = input("Enter a name: ")
station5_output = solution_station_5(station5_input)
<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> a0195fdc006ab3a39557f4785009c3dcaac08ee9
print(f"Team for {station5_input}: {station5_output}")
=======
print(f"Team for {station5_input}: {station5_output}")
>>>>>>> d684b8da1c9b12c240c5bef89019a2baf82bfcf8
