# Задание № 1
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person

print(name, last_name, city, phone, country)

# Задание № 2
result1 = 'результат операции: 42'
result2 = 'результат операции: 514'
result3 = 'результат работы программы: 9'

index = result1.index(':')
number = int(result1[index + 2:])
print(number + 10)

index = result2.index(':')
number = int(result2[index + 2:])
print(number + 10)

index = result3.index(':')
number = int(result3[index + 2:])
print(number + 10)

# Задание № 3
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

print('Students', ', '.join(students), 'study these subjects:', ', '.join(subjects))
