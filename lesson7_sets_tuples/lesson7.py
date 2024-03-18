# sets
set_test = {1,}
print(type(set_test))
set_test = set()
print(type(set_test))

some_set = {'1', '2', '2', '3'}
some_set1 = set(['a', 'b', 'b', 'c'])
some_set2 = set('Hello3')
some_set3 = {'1', '2', '2', '3'}

print(some_set1)
print(some_set2)

print('W' in some_set2)
print('l' in some_set2)

some_frozenset = frozenset('Frozen')
print(some_frozenset)

some_set.discard('2')  # удаление без ошибки, если элемент не найден
print(some_set)
# some_set.remove('6') # удаление с ошибкой если элемент не найден

some_set.add('7')
some_set_union = some_set.union(some_set1)
print('union: ', some_set_union)
print('union with |: ', some_set | some_set1)
some_set |= some_set1 # объединение в первый сет
print(some_set)

# пересечение сетов
print(some_set.intersection(some_set2))
print(some_set & some_set2 & some_set1)

print(' difference: ', some_set3.difference(some_set2)) # различия

set_1 = {'1', '2', '3'}
set_2 = {'1', '2', '3', '4'}
print(set_1.issubset(set_2)) # элементы 1го входят во 2й

print(set_1.symmetric_difference(set_2))
print(set_1 ^ set_2)

print('\n\n', '=' * 20, '\n', '=' * 20)
print('TUPLES')

tuple_1 = ()
tuple_2 = tuple()
tuple_3 = tuple('Hello I am python developer')

print(tuple_3.count('l'))
print(tuple_3.index('l'))

# получение данных в переменные!!!!!!!
a, b, c = (1, 2, 3)
print(a,b,c)

# сваппинг 2х переменных
a = 1
b = 2
print(a,b)
a, b = b, a
print(a, b)

# распаковка значений
a, b, *anything = (b, a, 5, 7, 'myTExt') # нужно только 1х 2
print(f'{a=} {b=} {anything=}')

first, *middle, last = (b, a, 5, 7, 'myTExt')
print(f'{first=}, {middle=}, {last}')

class_school = (('Igor', 10), ('Mark', 8), ('Lena', 12), ('Zurab', 11))
for student in class_school:
    print(student)

for student, mark in class_school:
    print(f'{student=}, {mark=}')




