x = 1
y = 2
def print_x():
    print(x)


def print_namespaces():
    age = 23
    num = 56
    name = 'First'
    print('locals', locals())
    print('global variables', globals())


def external():
    def intrenal():
        return 1
    return intrenal()

def changing_product():
    product = 'milk'
    print('local: ', product)

    def showing_enclosed():
        # nonlocal product # будет меняться влженное пространство имен (из родительской функции)
        global product # будет изменяться глобальное пространство имен
        product = ' cola'
        print('Enclosed scope: ', product)

    showing_enclosed()
    print(product, '---')

def power(x, y):
    return x**y

def rectangle_area(height: int, length:int) -> int:
    return height * length


def natural_int(n: int) -> None:
    if n >= 1:
        natural_int(n - 1)
        print(n)


print_x()

print_namespaces()

# вложенные функции
print(external())

product = 'bread'
changing_product()
print('global: ', product)

# вызов функции без скобок - получаем объект функции
print(print_namespaces.__name__)
# встроенные функции python

# анонимные функции
# lambda!!!!
l = lambda x: x*5   # слева аргумент, справа - что возвращаем
print('lambda result: ', l(2))
print(l.__name__)

print('\n******* lambda example\n')
print(power(2,8))

p = lambda x, y: x**y
print(p(2,8))

# на примере сортировки
m = [4, 5, 2 , 7, 3, 10, 1]
m.sort()
print(m)
m.sort(key=lambda x:-x)
print(m)

z = list(map(lambda elem: elem**2, m))
print(z)

print('rectangle_area: ', rectangle_area(2, 5))

rectangle_area_lambda = lambda h, l: h*l
print(rectangle_area_lambda(2,7))

# рекурсия
print('******************рекурсия')
natural_int(12)