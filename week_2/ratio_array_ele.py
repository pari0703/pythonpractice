#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    sum1=0
    sum2=0
    sum3=0
    ele=len(arr)
    for i in range(ele):
        if arr[i]>0:
            sum1 += 1
        elif arr[i]<0:
            sum2 += 1
        elif arr[i] == 0:
            sum3 += 1
    print(format(sum1/ele, '.6f'))
    print(format(sum2/ele, '.6f'))
    print(format(sum3/ele, '.6f'))
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
