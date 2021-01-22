v_str = 'Строка'
v_int = 240
v_float = 240.0

print(type(v_str))
print(type(v_int))
print(type(v_float))

v_str = 'Строка'
v_int = 240 / 2
v_float = 240.0

print("Тип переменной v_str: " + str(type(v_str)))
print("Тип переменной v_int: " + str(type(v_int)))
print("Тип переменной v_float: " + str(type(v_float)))

v_str = 'Строка'
v_int = 240 / 2
v_float = 240.0

message = "Значение переменной 'v_float': " + str(v_int) + ". Тип: " + str(type(v_int))

print(message)

a = input('Введите значение переменной "a": ')
b = input('Введите значение переменной "b": ')

summ = int(a) + float(b)
dif = int(a) - int(b)

print(type(summ))
print(type(dif))

print('сумма a и b = ' + str(summ))
print('разность a и b = ' + str(dif))
print('b в квадрате = ' + str(int(b)**2))
print('если b разделить на цело на 2, то получится: ' + str(int(b)//2))
print('остаток от деления b на 2 = : ' + str(int(b)%2))

f = 24
g = 0

try:
    result = f/g
except ZeroDivisionError: # обработка ошибки деления на ноль
    print('Нельзя делить на 0')
    result = 0
except TypeError: # обработка ошибки несоответствия типов
    print('Ошибка типов - все операнды формулы должны быть числом. Присутствует операнд с типом не число.')
    result = 0
except: # обработка всех остальных ошибок
    print('Какая-то неизвестная ошибка')
    result = 0

print('Результат деления: ' + str(result))
