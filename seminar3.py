from math import pi as PI

class Shape:
    def __init__(self):
        raise TypeError("Попытка создания абстрактного класса")
    
    def get_area(self):
        raise TypeError("Попытка вызова абстрактного метода")
    
    def get_perimeter(self):
        raise TypeError("Попытка вызова абстрактного метода")
    
class Circle(Shape):
    def __init__(self, r):
        #super().__init__()
        self.r = int(r)
    
    def get_area(self):
        return PI * self.r ** 2
    
    def get_perimeter(self):
        return PI * self.r * 2
    
class Square(Shape):
    def __init__(self, a):
        #super().__init__()
        self.a = int(a)
    
    def get_area(self):
        return self.a ** 2
    
    def get_perimeter(self):
        return self.a * 4
    
class Triangle(Shape):
    def __init__(self, a, b, c):
        #super().__init__()
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)
    
    def get_area(self):
        return (self.a * self.b) / 2
    
    def get_perimeter(self):
        return self.a + self.b + self.c

def get_area(obj: Shape):
    return obj.get_area()

def get_perimeter(obj: Shape):
    return obj.get_perimeter()

ci = Circle(3)
sq = Square(4)
tr = Triangle(1,3,5)
#print("Площадь ", a.get_area())
#print("Периметр ", a.get_perimeter())

print("Площадь круга: ", get_area(ci))
print("Периметр круга: ", get_perimeter(ci))
print("Площадь квадрата: ", get_area(sq))
print("Периметр квадрата: ", get_perimeter(sq))
print("Площадь треугольника: ", get_area(tr))
print("Периметр треугольника: ", get_perimeter(tr))