def solution_station_4(numb):
    for i in range(2, numb):
        if (numb%i)==0:
            return False
    return True


