def bubbleSorting(A):
    for i in range(len(A) - 1):
        for j in range(len(A) - 2, i - 1, -1):
            if A[j + 1] < A[j]:
                A[j], A[j + 1] = A[j + 1], A[j]
    return A


A = list(map(int, input().split()))
print(bubbleSorting(A))