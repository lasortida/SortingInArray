def bubbleSorting(A):
    for i in range(len(A) - 1, 0, -1):
        max = i
        for j in range(i - 1, -1, -1):
            if A[j] > A[max]:
                max = j
        if (max != i):
            A[max], A[i] = A[i], A[max]
    return A



A = [7, 9, 0, 1, 2, -1, 0, 5, 21, 13]
print(bubbleSorting(A))