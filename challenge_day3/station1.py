x = int(input("Put in the number: "))

def solution_station_1 (x):
    n1 = 0
    n2 = 1
    count = 0

    if x < 0:
        x = int(input("Put in the number: "))
    if x == 0:
        print(f'{n1}')
    if x == 1:
        print(f'{n2}')

    else:
        while count < x:
            n = n1 + n2
            n1 = n2
            n2 = n
            count += 1
    return n1

result = solution_station_1(x)

print(result)


