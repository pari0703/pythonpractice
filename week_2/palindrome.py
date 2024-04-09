n = int(input())
integers = list(map(int, input().split()))
print(all(num > 0 for num in integers) and any(str(num) == str(num)[::-1] for num in integers))
