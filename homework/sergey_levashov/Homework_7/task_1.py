def guess_number():
    program_number = 8

    while True:
        guess_number = int(input('Угадайте цифру: '))
        if guess_number == program_number:
            print(f'Поздравляю! Вы угадали цифру: {guess_number}')
            break
        else:
            print('Попробуйте снова')


guess_number()
