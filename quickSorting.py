import random

def quickSorting(A):
    if len(A) <= 1:
        return A
    x = random.choice(A)
    B1 = [b for b in A if b < x]
    Bx = [b for b in A if b == x]
    B2 = [b for b in A if b > x]
    return quickSorting(B1) + Bx + quickSorting(B2)


A = list(map(int, input().split()))

print(quickSorting(A))