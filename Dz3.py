# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением
# дробной части элементов, отличной от 0.

# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

my_list = [1.1, 1.2, 3.1, 5, 10.01]
list2 = []
for i in range(len(my_list)):
    if my_list[i] % 1 != 0:
        list2.append(my_list[i])
list3 = [round(list2[i] % 1, 2) for i in range(len(list2))]
print(f"{list3} => {max(list3) - min(list3)}")