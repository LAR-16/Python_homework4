# Задача 24 про чернику
from random import randint
N = int(input("Введите количество кустов черники:"))
blueberry_bushes = []
for _ in range(N):
    number_of_berries = randint(1, 15)
    blueberry_bushes.append(number_of_berries)
print(blueberry_bushes)
sum_of_berries = 0
max_sum = 0
for i in range(N):
    if i == 0:
        sum_of_berries = blueberry_bushes[0] + \
            blueberry_bushes[1]+blueberry_bushes[-1]
        max_sum = sum_of_berries
    elif i > 0 and i <= N-2:
        sum_of_berries = blueberry_bushes[i] + \
            blueberry_bushes[i-1]+blueberry_bushes[i+1]
        if sum_of_berries > max_sum:
            max_sum = sum_of_berries
    elif i == N-1:
        sum_of_berries = blueberry_bushes[-1] + \
            blueberry_bushes[i-1]+blueberry_bushes[0]
        if sum_of_berries > max_sum:
            max_sum = sum_of_berries

print(f"Максимальное количество ягод: {max_sum}")
