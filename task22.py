# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

first_number =int(input("Введите количество элементов первого массива: "))
second_number =int(input("Введите количество элементов второго массива: "))
first_list=[]
second_list=[]
for _ in range(first_number):
    number=int(input("Введите число из первого массива:"))
    first_list.append(number)
print(first_list)

for _ in range(second_number):
    number=int(input("Введите число из второго массива:"))
    second_list.append(number)
print(second_list)

my_set=set()
for i in first_list:
    if i in second_list:
        my_set.add(i)
   
my_list=list(my_set)

for i in range(len(my_list)-1):
    for j in range(len(my_list)-1-i):
        if my_list[j] >my_list[j+1]:
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    
print(my_list)
