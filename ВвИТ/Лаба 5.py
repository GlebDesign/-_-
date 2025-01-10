class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f'Название книги: {self.title}, Автор: {self.author}, Год издания:  {self.year}'


x = Book("Дежавю", "Кизару", 2023)
print(x.get_info())


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, new_radius):
        self.radius = new_radius

# y = Circle(5)
# print(y.get_radius())
# y.set_radius(10)
# print(y.get_radius())