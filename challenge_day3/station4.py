<<<<<<< HEAD
<<<<<<< HEAD
=======
def solution_station_4(output4):
    if output4%2>0:
        print(True)
    else:
        print(False)
    return output4
=======
x = int(input("Enter a number: "))

def solution_station_4(numb):
    for i in range(2, numb):
        if (numb%i)==0:
            return print('False')
    return print('True')

numb = solution_station_4(x)
>>>>>>> a0195fdc006ab3a39557f4785009c3dcaac08ee9

>>>>>>> d684b8da1c9b12c240c5bef89019a2baf82bfcf8
