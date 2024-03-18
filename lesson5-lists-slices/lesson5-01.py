# списки
my_list = [1, 2, 3, 'hello']
print(my_list)
print(my_list[3])

list_empty = []

list1 = list()
list2 = list('hello')
print(list2)

colors: list = ['red', 'blue', 'green', 'black']
print('color ind=3', colors[3])
print('color ind=-3', colors[-3])
print(len(colors))

# срезы
easy = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(easy[2:7:2]) # вывод среза с инд. 2 по 7 с шагом 2
print(easy[-2: -100:-2]) # вывод среза справа на лево инд. 2 по 7 с шагом 2

# методы списков
print('*' * 20, 'methods')

shopping_list = ['milk', 'bread']
shopping_list.append('eggs')
print(shopping_list)
# shopping_list.clear()

print('--- extend')
shopping_list_weekly = ['milk', 'bread']
shopping_list_monday = ['eggs', 'potatoes']
shopping_list_tuesday = ['salt', 'meat']
shopping_list_weekly.extend(shopping_list_monday) # расширение списка добавлением
print(shopping_list_weekly)
shopping_list_weekly += shopping_list_tuesday # расширение списка сложением
print(shopping_list_weekly)

# получение индекса
print(shopping_list_weekly.index('salt'))

# pop()
food_list = shopping_list_weekly
deleted_element = food_list.pop()
print(deleted_element, food_list)
deleted_element = food_list.pop(3)
print(deleted_element, food_list)

# реверс / перевернуть список
food_list.reverse()
print(food_list)

# сортировка
food_list.sort()
print(food_list)
food_list.sort(reverse=True)
print(food_list)

# списки в цикле
print('*' * 20, 'списки в цикле')

for i in shopping_list_weekly:
    print(i)


for food in shopping_list_weekly:
    print(f'{shopping_list_weekly.index(food)+1}: {food}')

# удаление элементов списка

# Удалить все четные элементы списка
list_num = [2, 4, 1, 7, 3, 55, 98, 2, 12]
copy_list_num = list_num.copy() # копирование списка
index = 0
while True:
    if index < len(list_num):
        if list_num[index] % 2 ==0:
            copy_list_num.remove(list_num[index]) # удаляем значение
        index += 1
    else:
        break

print(copy_list_num)

# возвести все элементы в квадрат

new_list = []
for index in range(len(list_num)):
    list_num[index] = list_num[index] ** 2
print(list_num)

# НАЙТИ МАКСИМАЛЬНЫЙ ЭЛЕМЕНТ СПИСКА
# 1 variant
max_val = list_num[0]
for i in range(1, len(list_num)):
    if list_num[i] > max_val:
        max_val = list_num[i]
print("MAX = ", max_val)

# 2 variant
print(max(list_num))

# 3 variant
print('sort1', sorted(list_num)[-1])

# 4 variant
list_num.sort()
print(list_num[-1])

print('222222', list_num[:])



