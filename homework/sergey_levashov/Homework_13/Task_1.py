import os
from datetime import datetime, timedelta

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, '..', '..', 'eugene_okulik', 'hw_13', 'data.txt')

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()

        number, rest = [part.strip() for part in line.split('.', 1)]
        date_str, action = rest.split(' - ', 1)
        date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')

        if 'на неделю позже' in action:
            new_date = date_obj + timedelta(weeks=1)
            print(new_date)
        elif 'день недели' in action:
            print(date_obj.strftime('%A'))
        elif 'сколько дней назад' in action:
            today = datetime.now()
            delta = today - date_obj
            print(f"{delta.days} дней назад")
