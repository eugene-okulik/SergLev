def sum_function(line):
    print(int(line.split(':')[-1].strip()) + 10)


result = [
    'результат операции: 42',
    'результат операции: 54',
    'результат работы программы: 209',
    'результат: 2'
]

for line in result:
    sum_function(line)
