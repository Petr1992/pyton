# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

a =  [i ** 2  for i in [1, 2, 4, 0]]
print(a)


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

a = ['apple','orange','milk','orangje']
b = ['apple','orajnge']

c = [i  for i in a if i in b]
print(c)


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4



a = [2,5,14,10,5,2,3,9,16,-15,-9]
b= []
for i in range(len(a)):
    if (a[i] % 3 == 0) and (a[i]>0) and (a[i] % 4 != 0) :
        b.append(a[i])
print(b)