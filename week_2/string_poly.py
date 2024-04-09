x, k=list(map(int, input().split()))
poly=input()
integer= eval(poly.replace('x',str(x)))
if integer == k:
  print(True)
else:
  print(False)