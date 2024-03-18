# exceptions


def divide_two_numbers(first, second):
    try:
        answer = first / second
    except ZeroDivisionError:
        return "you couldn't divide on zero"
    except (TypeError, Exception):  # в скобках можно указать список исключений для обработки. "Exception" - базовое исключение
        return "wrong value type (num / str)"
    else:   # выполяется, если небыло ошибок/исключений
        print('else')
    finally: # выполняется в любом случае (имеет макс.приоритет перед остальными ветками
        return 'FINALLY'

    return answer


def bool_return():
    try:
        return  True
    finally:
        return False



print(divide_two_numbers(1, 0))

print('result with FINALLY: ', bool_return())

# rise - поднятие ошибки

try:
    raise ZeroDivisionError
except:
    print('I catch raised error')


# # assert - ложно, неверно
# assert 1==1
# assert 1==2
#
# if 1!=2:
#     raise AssertionError
#
# assert 1==2

print('\n', '-'*20)
"""функция принимает номер месяца и выводит его название"""
def month_name(month_number):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
    try:
        month_index = abs(month_number) - 1    # берем число по модулю во избежание отрицательных значений
        return months[month_index]
    except TypeError as e:
        print(f'Error message: {e}')
        return 'use integers only'
    except IndexError as e:
        return 'only integers 1 - 12'



print(month_name('ffdfdf'))
assert month_name(1) == 'Jan'  # проверка корректности работы


"""проверить все ли числоа последовательности являются уникальными и реализовать несколько обработок исключений"""
