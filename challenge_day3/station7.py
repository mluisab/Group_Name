equation = input("Enter an equation: ")

def solution_station_7():
   a=3
   b=-1
   c=4
   d=7
   e=0.5
   answer= eval(equation, {'a':a, 'b':b, 'c':c, 'd':d, 'e':e})
   return answer
print(solution_station_7())
