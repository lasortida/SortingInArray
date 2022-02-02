from random import randint

countChance = 0
countBubble = 0
sumChance = 0
sumBubble = 0

def chanceSorting(A, countChance):
    for i in range(len(A) - 1):
        min = i
        for j in range(i + 1, len(A)):
            if A[j] < A[min]:
                min = j
        if i != min:
            A[i], A[min] = A[min], A[i]
            countChance += 1
    return A, countChance


def bubbleSorting(A, countBubble):
    for i in range(len(A) - 1):
        for j in range(len(A) - 2, i - 1, -1):
            if A[j + 1] < A[j]:
                A[j], A[j + 1] = A[j + 1], A[j]
                countBubble += 1
    return A, countBubble


# A = [0] * 1000
# B = [0] * 1000
# for i in range(1000):
#     x = randint(0, 10000)
#     A[i] = x
#     B[i] = x


# print(f"Выборка - {chanceSorting(A, countChance)[1]}")   #Кол-во
# print(f"Пузырёк - {bubbleSorting(B, countBubble)[1]}")

for i in range(100):
    A = [0] * 1000
    B = [0] * 1000
    for i in range(1000):
        x = randint(0, 10)
        A[i] = x
        B[i] = x
    countChance = chanceSorting(A, countChance)[1]
    countBubble =  bubbleSorting(B, countBubble)[1]
    sumBubble += 1
    sumChance += 1

print(f"Пузырёк - {countBubble / sumBubble}")
print(f"Выборка - {countChance / sumChance}")