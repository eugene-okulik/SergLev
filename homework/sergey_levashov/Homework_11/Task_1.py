class Books:
    material = 'бумага'
    text = True

    def __init__(self, book_name, author, numbers_of_pages, isbn, reserved=False):
        self.book_name = book_name
        self.author = author
        self.numbers_of_pages = numbers_of_pages
        self.isbn = isbn
        self.reserved = reserved

    def print_this_book(self):
        if self.reserved:
            print(
                f'Название: {self.book_name}, Автор: {self.author}, страниц: {self.numbers_of_pages},'
                f' материал: {Books.material}, зарезервирована'
            )
        else:
            print(
                f'Название: {self.book_name}, Автор: {self.author}, страниц: {self.numbers_of_pages},'
                f' материал: {Books.material}'
            )


class SchoolBooks(Books):
    def __init__(self, book_name, author, numbers_of_pages, isbn, subject, school_grade, exercise=False, reserved=False
                 ):
        super().__init__(book_name, author, numbers_of_pages, isbn, reserved=reserved)
        self.subject = subject
        self.school_grade = school_grade
        self.exercise = exercise

    def print_this_school_book(self):
        if self.reserved:
            print(
                f'Название: {self.book_name}, Автор: {self.author}, '
                f'страниц: {self.numbers_of_pages}, предмет: {self.subject}, '
                f'класс: {self.school_grade}, зарезервирована'
            )
        else:
            print(
                f'Название: {self.book_name}, Автор: {self.author}, '
                f'страниц: {self.numbers_of_pages}, предмет: {self.subject}, класс: {self.school_grade}'
            )


book1 = Books('Мастер и Маргарита', 'Булгаков', 500, 123456)
book2 = Books('Преступление и наказание', 'Достоевский', 300, 12345)
book3 = Books('Война и мир', 'Толстой', 1000, 1234567, reserved=True)
book4 = Books('1984', 'Оруэлл', 450, 123)
book5 = Books('Скотный двор', 'Оруэлл', 400, 12345678)

book1.print_this_book()
book2.print_this_book()
book3.print_this_book()
book4.print_this_book()
book5.print_this_book()

school_book1 = SchoolBooks(
    'Биология 8 класс', 'Великий Биолог', 1500, 123456,
    'Биология', 8
)

school_book2 = SchoolBooks(
    'Супер-пупер программист', 'ИИ', 10, 134523456,
    'Информатика', 11
)

school_book3 = SchoolBooks(
    'Как стать трудовиком и не спится', 'Гаврила', 100, 1,
    'Труд', 10, reserved=True
)

school_book1.print_this_school_book()
school_book2.print_this_school_book()
school_book3.print_this_school_book()
