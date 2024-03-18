def print_sum(a, b):
    print(2+2)

def example():
    pass  # заглушка

def example2():
    ... # заглушка

def example3():
    # заглушка
    """какойто текст в качестве заглушки"""


def printing_positional_arguments(first, second):
    print(f'{first=}, {second=}')

def print_args1(a, b, *args):
    print(a, b, args)

def make_pizza(*toppings):
    for topping in toppings:
        print(f'{topping=}')


def printing_positional_arguments2(first, second, third):
    print(f'{first=}, {second=}, {third=}')

# параметр со значением по-умолчанию
def hello_user(job_position, name, surname, middlename=''):
    print(f'Hello {name} {surname} {middlename}. your job position is {job_position}')

def hello_user2(job_position, name, surname, middlename='', **kwargs):
    print(kwargs)
    print(f'Hello {name} {surname} {middlename}. your job position is {job_position}')


def sum_two_numbers(a, b):
    return a + b


def external():
    def internall():
        pass

    return internall


# позиционные аргументы
print_sum(3, 7)

printing_positional_arguments('1st', '2nd')

print_args1('a', 'b', 'c', 'd', 'e', 'f')

make_pizza('mushrooms', 'sausages', 'chees', 'capers')


# ключевые аргументы
printing_positional_arguments2(third='3th', second='2nd', first='1st')

# использование разных аргументов: сначала позиционные. потом ключевые

hello_user('programmer', surname='Dil', name='Mark')

# упаковка аргументов в словарь
hello_user2('programmer', surname='Dil', name='Mark', country='Ukraine', car='CAT')

# return
result = sum_two_numbers(5, 8)
print(result)

# вложенные функции
print(type(external()))