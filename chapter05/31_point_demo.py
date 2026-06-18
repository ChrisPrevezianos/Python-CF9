import math
 
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x # call the setter
        self.y = y
   
    @property
    def x(self):
        return self._x
   
    @x.setter
    def x(self, value):
        if not isinstance(value, float):
            raise ValueError("x must be a number")
        self._x = value
 
    @property
    def y(self):
        return self._y
   
    @y.setter
    def y(self, value):
        if not isinstance(value, float):
            raise ValueError("y must be a number")
        self._y = value
   
    @property
    def distance_from_origin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
   
    def move(self, dx, dy):
        self._x += dx
        self._y += dy
   
    def __str__(self):
        return f"Point(x={self.x}, y={self.y})"


def main():
    p = Point(3.0, 4.0)
    print(p)
    print(p.x, p.y)
    print(p.distance_from_origin)

    p.move(2.0, 1.0)
    print(p)

    # p.distance_from_origin = 100

    # p.x = "Prevezianos"

if __name__ == "__main__":
    main()