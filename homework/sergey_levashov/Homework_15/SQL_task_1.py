import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)
cursor = db.cursor(dictionary=True)
# 1. Создание студента
cursor.execute("""
    INSERT INTO students (name, second_name, group_id)
    VALUES (%s, %s, %s)
""", ('SERG17', 'SqlPython', None))
db.commit()

# Получение ID созданного студента
cursor.execute("SELECT * FROM students WHERE name LIKE 'SERG17'")
student = cursor.fetchone()
student_id = student['id']
print("Создан студент:", student)

# 2. Создание книг и привязка к студенту
books = [
    ('Математика для чайников999', student_id),
    ('Информатика999', student_id),
    ('История Питона999', student_id)
]
cursor.executemany("""
    INSERT INTO books (title, taken_by_student_id)
    VALUES (%s, %s)
""", books)
db.commit()

# Проверка книг студента
cursor.execute("SELECT * FROM books WHERE taken_by_student_id = %s", (student_id,))
print("Книги студента:", cursor.fetchall())

# 3. Создание группы
cursor.execute("""
    INSERT INTO `groups` (title, start_date, end_date)
    VALUES (%s, %s, %s)
""", ('Группа AQAPython', '2025-10-15', '2025-11-15'))
db.commit()

# Получение ID группы
cursor.execute("SELECT * FROM `groups` WHERE title LIKE %s", ('%Группа AQAPython%',))
group = cursor.fetchone()
group_id = group['id']
print("Создана группа:", group)

# Обновление группы у студента
cursor.execute("""
    UPDATE students
    SET group_id = %s
    WHERE id = %s
""", (group_id, student_id))
db.commit()

# 4. Создание предметов
subjects = [
    ('Обучение автоматизации Python',),
    ('Обучение SQL',)
]
cursor.executemany("INSERT INTO subjects (title) VALUES (%s)", subjects)
db.commit()

# Получение ID предметов
cursor.execute("""
    SELECT * FROM subjects
    WHERE title IN ('Обучение автоматизации Python', 'Обучение SQL')
""")
subjects_data = cursor.fetchall()
subject_ids = {sub['title']: sub['id'] for sub in subjects_data}
print("Созданные предметы:", subjects_data)

# 5. Добавление занятий
lessons = [
    ('Супер автотесты', subject_ids['Обучение автоматизации Python']),
    ('Pytest в жизни', subject_ids['Обучение автоматизации Python']),
    ('История питонов', subject_ids['Обучение SQL']),
    ('Современные змеи', subject_ids['Обучение SQL'])
]
cursor.executemany("""
    INSERT INTO lessons (title, subject_id)
    VALUES (%s, %s)
""", lessons)
db.commit()

# Получение ID занятий
cursor.execute("""
    SELECT * FROM lessons
    WHERE subject_id IN (%s, %s)
""" % (subject_ids['Обучение автоматизации Python'], subject_ids['Обучение SQL']))
lessons_data = cursor.fetchall()
lesson_ids = {lesson['title']: lesson['id'] for lesson in lessons_data}
print("Созданные занятия:", lessons_data)

# 6. Выставление оценок студенту
marks = [
    (5, lesson_ids['Супер автотесты'], student_id),
    (5, lesson_ids['Pytest в жизни'], student_id),
    (4, lesson_ids['История питонов'], student_id),
    (4, lesson_ids['Современные змеи'], student_id)
]
cursor.executemany("""
    INSERT INTO marks (value, lesson_id, student_id)
    VALUES (%s, %s, %s)
""", marks)
db.commit()

# Получение всех оценок студента
cursor.execute("""
    SELECT m.value AS mark, l.title AS lesson_title
    FROM marks m
    JOIN lessons l ON m.lesson_id = l.id
    WHERE m.student_id = %s
""", (student_id,))
print("Оценки студента:", cursor.fetchall())

# Получение всех книг студента
cursor.execute("""
    SELECT title AS book_title
    FROM books
    WHERE taken_by_student_id = %s
""", (student_id,))
print("Книги студента:", cursor.fetchall())

# Полная информация о студенте
cursor.execute("""
    SELECT
        s.name,
        s.second_name,
        g.title AS group_title,
        b.title AS book_title,
        sub.title AS subject_title,
        l.title AS lesson_title,
        m.value AS mark
    FROM students s
    LEFT JOIN `groups` g ON s.group_id = g.id
    LEFT JOIN books b ON s.id = b.taken_by_student_id
    LEFT JOIN marks m ON s.id = m.student_id
    LEFT JOIN lessons l ON m.lesson_id = l.id
    LEFT JOIN subjects sub ON l.subject_id = sub.id
    WHERE s.id = %s
""", (student_id,))
print("Полная информация о студенте:", cursor.fetchall())

db.close()
