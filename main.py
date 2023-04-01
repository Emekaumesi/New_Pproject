from rectangle import rectangle
from triangle import triangle

rect = rectangle()
tri = triangle()
rect.set_values(30, 50)
tri.set_values(200, 500)
rect.set_colour('Green')
tri.set_colour('purple')

print(rect.area())
print(rect.get_colour())
print(tri.get_colour())