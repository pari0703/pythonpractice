A = []
B = []
C = []

# Input dimensions of matrices
n1 = int(input("Enter the number of rows for matrix A: "))
m1 = int(input("Enter the number of columns for matrix A: "))
n2 = int(input("Enter the number of rows for matrix B: "))
m2 = int(input("Enter the number of columns for matrix B: "))

# Check if matrices can be multiplied
if m1 != n2:
    print("Matrix multiplication not possible.")
else:
    # Input elements for matrix A
    print("Enter elements for matrix A:")
    for i in range(n1):
        A.append(list(map(int, input().split())))

    # Input elements for matrix B
    print("Enter elements for matrix B:")
    for i in range(n2):
        B.append(list(map(int, input().split())))

    # Initialize result matrix C with zeros
    for i in range(n1):
        C.append([0] * m2)

    # Perform matrix multiplication
    for i in range(n1):
        for j in range(m2):
            for k in range(m1):
                C[i][j] += A[i][k] * B[k][j]

    # Output the result matrix C
    print("Result of matrix multiplication:")
    for i in range(n1):
        for j in range(m2):
           print(C[i][j],end=' ')
        print()
    
