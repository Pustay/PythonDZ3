# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

fibonachi = int(input('Введите число: '))
my_list = []
for i in range(fibonachi+1):
    if i==0:
        my_list.append(i)
    elif i==1:
        my_list.append(i)
        my_list.insert(0, i)
    else:
        my_list.append(my_list[len(my_list)-1]+my_list[len(my_list)-2])
        my_list.insert(0, (-1)**(i-1)*my_list[len(my_list)-1])
print(my_list)