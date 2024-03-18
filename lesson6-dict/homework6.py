d = {'a':3, 'b':0, 'c':4, 'd':-3}
max_val = d['a']
max_owner = 'a'
for key, value in d.items():
    if value > max_val:
        max_val = value
        max_owner = key

print(f'max value: key {max_owner}: {max_val}')

d = {'a':3, 'b':'hello', 'c':4, 'd':-3}
val_list = []

for key, value in d.items():
    # val_list.append(value)
    if ord(str(value)[0]) > ord(str(max_val)[0]):
        max_val = value
        max_owner = key

print(f'max value in key {max_owner}: {max_val}')
