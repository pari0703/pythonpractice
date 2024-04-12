# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

ab = int(input())
bc = int(input())

hypo = math.sqrt(ab**2 + bc**2)
angle = math.degrees(math.asin(ab/hypo))

print(round(angle),"\u00b0")