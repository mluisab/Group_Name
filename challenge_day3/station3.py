
def solution_station_3(x):
    return x % 3 == 0

number = int(input("Please enter a number"))

answer = solution_station_3(number)
print(answer)