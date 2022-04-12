from rectangle import Rectangle, Square, Circle, Triangle

# Создание прямоугольников

r1 = Rectangle(2, 5)
r2 = Rectangle(3, 7)

# Вывод площади прямоугольников

print("Площадь 1 прямоугольника: ", r1.get_area())
print("Площадь 2 прямоугольника: ", r2.get_area())

# Создание квадратов

s1 = Square(5)
s2 = Square(10)

# Вывод площади квадратов

print("Площадь 1 квадрата", s1.get_square())
print("Площадь 2 квадрата", s2.get_square())

c1 = Circle(2)
c2 = Circle(3)

print("Площадь круга", c1.get_area_circle())
print("Площадь круга", c2.get_area_circle())

t1 = Triangle(2, 6)
t2 = Triangle(3, 4)

print("Площадь треугольника", t1.get_area_triangle())
print("Площадь треугольника", t2.get_area_triangle())
print(t1.get_triangle_args())   # Вызов метода для возвращения параметров фигуры в строку

# Теперь мы хотим в нашей программе все объекты перенести в единую коллекцию. Назовем фигуры (figures).
# Коллекция содержит список, в который мы помещаем наш первый прямоугольник, квадрат и т.д.

figures =[r1, r2, s1, s2, c1, c2, t1, t2]

# Далее пройдемся по циклу for:
# Это необходимо, чтобы найти площадь каждой фигуры, сохраненной в списке figures.
# Обратите внимание, мы будем работать с прямоугольниками и квадратами с помощью разных методов:
# get_area() и get_area_square().
# Внутри цикла проверяем:
# Если экземпляр класса figure является квадратом, то вызываем метод get_area_square().
# В противном случае — обрабатываем данные для прямоугольника методом get_area().

for fig in figures:
    if isinstance(fig, Square):                             # функция isinstance проверяет, является ли аргумент объекта
        print("Площадь квадрата: ", fig.get_square())       # экземпляром класса или экземпляром класса из кортежа.
    elif isinstance(fig, Circle):                           # функция isinstance проверяет, является ли аргумент объекта
        print("Площадь круга", fig.get_area_circle())       # В случае если является, функция возвращает True, если не является — False.
    elif isinstance(fig, Triangle):
        print("Площадь треугольника", fig.get_area_triangle())
    else:
        print("Площадь прямоугольника: ", fig.get_area())


