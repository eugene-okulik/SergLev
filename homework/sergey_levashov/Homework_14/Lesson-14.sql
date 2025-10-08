-- 1. создаю студента
INSERT INTO students (name, second_name, group_id)
VALUES ('SERG', 'AQA', 2);

-- посмотреть созданого студента и взять его id = 21508
SELECT *
FROM students
WHERE name like 'SERG'

-- 2. создать книги и указать что студент SERG (id = 21508) взял их
INSERT INTO books (title, taken_by_student_id)
VALUES 
  ('Математика для чайников', 21508),
  ('Информатика', 21508),
  ('История Питона', 21508);

-- посмотреть какие книги есть у студента
SELECT *
FROM books b 
WHere b.taken_by_student_id = 21508

-- 3. создание группы
INSERT INTO `groups` (title, start_date, end_date)
VALUES ('Группа AQA', 'oct 2025', 'now 2025' );

-- проверяю созданную группу и беру ее id = 21448
SELECT *
FROM `groups` 
where title like '%Группа AQA%'

-- помещение студента в новую группу
UPDATE students
SET group_id = 21448
WHERE id = 21508;

-- 4. создание нескольких учебных предметов
INSERT INTO subjects (title)
VALUES ('Обучение автоматизации'),
	   ('Трактороведение');

-- посмотреть созданные предметы Обучение_автоматизации_id = 12636, Трактороведение_id = 126637
SELECT *
FROM subjects 
WHERE title in ('Обучение автоматизации','Трактороведение')


-- 5. добавить по два занятия в каждый предмет
INSERT INTO lessons (title, subject_id)
VALUES 
  ('Введение в автотесты', 12636),
  ('Pytest на практике', 12636),
  ('История тракторов', 12637),
  ('Современные тракторы', 12637);

-- посмотреть созданные занятия
SELECT *
FROM lessons l 
WHERE l.subject_id in (12636, 12637)

-- 6. поставить оценки студенту c id = 21508 (студент не тракторист)
INSERT INTO marks (value, lesson_id, student_id)
VALUES 
  (5, 13374, 21508),
  (5, 13375, 21508),
  (3, 13376, 21508),
  (2, 13377, 21508);

-- получить все оценки студента
SELECT m.value AS mark, l.title AS lesson_title
FROM marks m
JOIN lessons l ON m.lesson_id = l.id
WHERE m.student_id = 21508;

-- получить все книги которые есть у студента
SELECT title AS book_title
FROM books
WHERE taken_by_student_id = 21508;

-- полная информация о студенте 
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
WHERE s.id = 21508;
