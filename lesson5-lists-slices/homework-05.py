import turtle

# Завдання 1
# Є список а = [2, 4, 65, 32, 2, 6, 0, -1, 3]. Вивести всі значення менше 5 у консоль.

a = [2, 4, 65, 32, 2, 6, 0, -1, 3]
for i in range(len(a)):
    if a[i] < 5:
        print(a[i], end=', ')

# Завдання 2
# "aabbаа" - паліндром. Як це перевірити?
print('\n\n', '*'*10, 'TASK 2', '*'*10)

word = "aabbaa"
list = list(word)
print(list)
list_reverse = list.copy()
list_reverse.reverse()
print(list_reverse)
if list == list_reverse:
    print(f'word {word} is palindrom')
else:
    print(f'word {word} IS NOT palindrom')

# Завдання 3
# На основі списку a = ['red', 'yellow', 'blue', 'bread']
# Створити список, у якому буде лише слово, зайве у списку a.
print('\n\n', '*'*10, 'TASK 3', '*'*10)
col = turtle.color('red')
print(turtle.color('red'))



