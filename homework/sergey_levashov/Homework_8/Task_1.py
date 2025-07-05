import random

salary = int(input("Введите зарплату: "))

bonus = random.choice([True, False])

if bonus:
    bonus_amount = random.randint(1, 5000)
    salary += bonus_amount

print(f"${salary}")
