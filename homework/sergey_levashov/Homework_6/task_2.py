range(1, 101)
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print('FuzzВuzz')
    elif num % 3 == 0:
        print('Fuzz')
    elif num % 5 == 0:
        print('Вuzz')
    else:
        print(num)
