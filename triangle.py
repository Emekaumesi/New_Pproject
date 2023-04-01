from POLYGON import polygon
from shape import Shape

class triangle(polygon, Shape):
    def area(self):
        return self.get_width() * self.get_height() / 2