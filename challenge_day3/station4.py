
x = int(input("Enter a number: "))

def solution_station_4(numb):
    for i in range(2, numb):
        if (numb%i)==0:
            return print('False')
    return print('True')

numb = solution_station_4(x)

