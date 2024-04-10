from collections import defaultdict

# Read input
n, m = map(int, input().split())

# Initialize defaultdict to store positions of words in group A
positions = defaultdict(list)

# Store positions of words in group A
for i in range(1, n+1):
    word = input().strip()
    positions[word].append(i)

# Check positions of words in group B
for i in range(m):
    word = input().strip()
    if word in positions:
        print(*positions[word])
    else:
        print(-1)
