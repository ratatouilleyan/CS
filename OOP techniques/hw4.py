class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'{self.x}, {self.y}'
    def if_on_x_axis(self):
        return self.y == 0
    def __eq__(self, value):
        return self.x == value.x and value.y == self.y
    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
    def if_in_unit_circle(self):
        return self.distance(Point(0, 0)) <= 1
    def find_midpoint(self, other):
        return Point((self.x + other.x) / 2, (self.y + other.y) / 2)

point1 = Point(1, 2)
point2 = Point(3, 4)
print(point1)
print(point2)
print(point1.if_on_x_axis())
print(point1 == point2)
print(point1.distance(point2))
print(point1.if_in_unit_circle())
print(point1.find_midpoint(point2))