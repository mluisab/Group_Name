def solution_station_4(numb):
    if numb==1:
        return False
    for i in range(2, numb):
        if (numb%i)==0:
            return False
    return True


