#!/bin/python3
from datetime import datetime
# Complete the time_delta function below.
def time_delta(t1, t2):
    datetime1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    datetime2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    time_diff = abs(datetime1 - datetime2).total_seconds()
    return int(time_diff)
if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        print(str(delta) + '\n')

   
