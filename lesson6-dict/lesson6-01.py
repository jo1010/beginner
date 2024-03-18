# dictionaries

dict1 = {'key1':'value1'}

# create
# v1
dict2 = {
    'key1': 'value1',
    'key2': 'value2',
}

# v2
dict3 = dict([['key1', 'value1'], ['key2', 'value2']])

# v3
dict4 = dict(key1='value1', key2='value2')
print(dict4)


# getting data
print(dict4['key2'])

# add data
dict4['key3'] = 'value3'
print(dict4)

# create empty
my_dict = {}
my_dict: dict = dict()

cities: dict = dict()
cities['Kiyiv'] = 879
cities['Kharkiv'] = 1638
print(cities)
cities['Kiyiv'] = {'Year of foundation' : 879, 'Main revers' : ['Dnipro', 'Other']}
print(cities)

# delete
del cities['Kharkiv']
print(cities)

# ******
# work with data
# v1
for element in dict4:
     print(element, dict4[element])

# v2
for key, value in dict4.items():
    print(f'V 2 {key} - {value}')

print(dict4.items())

dict5 = dict4.copy()
print('befor clear', dict5)
dict5.clear()
print('after clear', dict5)

# pop
example_dict = dict4.copy()
print(example_dict.pop('key2'))
print(example_dict)

# popitem() - deletes last element
print(example_dict.popitem())
print(example_dict)

# update
example_dict.update({'key5':'value5'})
example_dict.update({'key6':'value6'})
print(example_dict)

# values
values_of_dict = example_dict.values();
print(values_of_dict)

# keys
keys_of_dict = example_dict.keys();
print(keys_of_dict)

# setdefault  -получение значения по умолчанию, если не найдено
print('GET: ', example_dict.get('Key15'))
print('SETDEFAULT: ', example_dict.setdefault('Key15', 'default value if not found'))

# fromkeys  -создание словаря на основании списка/кортежа со значением по умолчанию
empty_dict: dict = dict()
week_days = ['Mon', 'Tue', 'Wed']
new_dict = empty_dict.fromkeys(week_days, 'default value')
print(new_dict)
new_dict = empty_dict.fromkeys(range(40), 'any value')

print('\n\n','='*20)
print('\n', '*'*10, 'TASK 1', '*'*10)
# посчитать при помощи словаря сколько раз элемент повторяется в списке

classmates_name = ['Igor', 'Sasha', 'Dima', 'Igor', 'Lena', 'Igor', 'Dima']

# v1
answer = {}
for name in classmates_name:
    if name in answer.keys():
        answer[name] += 1
    else:
        answer[name] = 1

print('answer: ', answer)

# v2
answer = {}
for name in classmates_name:
    answer[name] = classmates_name.count(name)

print(answer)

print('\n', '*'*10, 'TASK 2', '*'*10)
# пройтись по словарю и выбрать значения, у которых четный ключ

data_dict = {1: 11, 33: 'tri-tri', 6: 66, 12: 'twelve'}
for key, value in data_dict.items():
    if key % 2 ==0:
        print(value)

print('\n', '*'*10, 'TASK 3', '*'*10)
# удалить все ключи, названия которых начинаются с буквы

data_dict = {1: 11, '33': 'tri-tri', 6: 66, '12': 'twelve'}
data_dict_copy = data_dict.copy()

for k in data_dict.keys():
    if type(k) == str:
        del data_dict_copy[k]

print(data_dict_copy)


