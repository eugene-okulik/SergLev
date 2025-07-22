def operation(func):
    def wrapper(first, second, operation=None):
        if first < 0 or second < 0:
            operation = '*'
        elif first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif second > first:
            operation = '/'
        return func(first, second, operation)

    return wrapper


@operation
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        if second == 0:
            return "Ошибка: деление на ноль"
        return first / second
    else:
        return "Неизвестная операция"


a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

result = calc(a, b)
print("Результат:", result)
