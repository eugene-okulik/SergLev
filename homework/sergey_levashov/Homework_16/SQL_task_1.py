import os
import csv
import mysql.connector as mysql
import dotenv

# Путь к CSV-файлу
csv_file_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '..', '..', 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv'
)
csv_file_path = os.path.normpath(csv_file_path)

# Подключение к базе
dotenv.load_dotenv(override=True)

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)
cursor = db.cursor()

not_found = []

# чтение файла data и проверка каждой строчки по отдельности
with open(csv_file_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        query = """
        SELECT 1
        FROM students s
        LEFT JOIN `groups` g ON s.group_id = g.id
        LEFT JOIN books b ON s.id = b.taken_by_student_id
        LEFT JOIN marks m ON s.id = m.student_id
        LEFT JOIN lessons l ON m.lesson_id = l.id
        LEFT JOIN subjects sub ON l.subject_id = sub.id
        WHERE s.name = %s
          AND s.second_name = %s
          AND g.title = %s
          AND b.title = %s
          AND sub.title = %s
          AND l.title = %s
          AND m.value = %s
        LIMIT 1
        """
        values = (
            row['name'],
            row['second_name'],
            row['group_title'],
            row['book_title'],
            row['subject_title'],
            row['lesson_title'],
            row['mark_value']
        )
        cursor.execute(query, values)
        result = cursor.fetchone()
        if not result:
            not_found.append(values)

# Вывод
if not_found:
    print("Не найдены в базе данных:")
    for row in not_found:
        print(row)
else:
    print("Все строки из CSV найдены в базе данных.")

cursor.close()
db.close()
