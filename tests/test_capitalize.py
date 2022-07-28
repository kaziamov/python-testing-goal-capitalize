from scr.capitalize import capitalize

if capitalize('hello') != 'Hello':
    raise Exception('Функция работает неверно!')

if capitalize('') != '':
    raise Exception('Функция работает неверно!')

if capitalize(' ') != ' ':
    raise Exception('Функция работает неверно!')

if capitalize('Hello') != 'Hello':
    raise Exception('Функция работает неверно!')

if capitalize('17') != '17':
    raise Exception('Функция работает неверно!')

print('Все тесты пройдены!')




