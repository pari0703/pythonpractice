A = set(map(int, input().split()))
n = int(input())

# Initialize a flag to track if A is a strict superset
is_strict_superset = True

# Loop through the sets
for _ in range(n):
    a = set(map(int, input().split()))
    # Check if A is not a superset of a or a is equal to A
    if not A.issuperset(a) or A == a:
        # A is not a strict superset, so set the flag to False and break the loop
        is_strict_superset = False
        break

# Print the result
print(is_strict_superset)
