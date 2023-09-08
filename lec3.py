import math

class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def __add__(self, other):
        return self.area + other.area

    def __eq__(self, other):
        return self.area == other.area

    def calc_area(self):
        self.area = self.width * self.length
        return self.area
    
    def calc_perimeter(self):
        self.perimeter = 2 * (self.width + self.length)
        return self.perimeter
    
    def calc_diag_len(self):
        self.diag = (self.width**2 + self.length**2)**0.5
        return self.diag
    
    def calc_diag_angles(self):
        """
        Calculates and returns two angles
        between the diagonals in degrees.
        """
        if not hasattr(self, 'diag'):
            self.calc_diag_len()
        cos_diag_length = self.length / self.diag
        angle_diag_length = math.acos(cos_diag_length)
        angle_diag_length = math.degrees(angle_diag_length)
        first_angle = 180 - (2*angle_diag_length)
        second_angle = (360 - 2*first_angle) / 2
        assert first_angle + second_angle == 180
        return first_angle, second_angle

r = Rectangle(3,4)
print(r.calc_area())
print(r.calc_perimeter())
print(r.calc_diag_len())
print(r.calc_diag_angles())
# print(type(r))

r1 = Rectangle(2,3)
r2 = Rectangle(4,7)
r1 = r1.calc_area()
r2 = r2.calc_area()
print(r1 == r2)
print(r1 + r2)
'''
w = r.width
l = r.length
print(w)
print(l)
'''