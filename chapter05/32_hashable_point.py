class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
   
    # def __eq__(self, other):
    #     # if not isinstance(other, Point):
    #     #     return False
    #     # return (self._x == other._x and self._y == other._y)
    #     return isinstance(other, Point) and self._x == other._x and self._y == other._y
   
    # def __hash__(self):
    #     return hash((self._x, self._y))
 
    def __str__(self):
        return f"({self._x}, {self._y})"
   
    def __repr__(self):
        return f"Point({self._x}, {self._y})"
   
 
def main():
    p1 = Point(1, 2)
    print(f"p1: {p1}")
    p2 = Point(3, 4)
    p3 = Point(1, 2)
 
    print(f"p1 == p2: {p1 == p2}")
    print(f"p1 == p3: {p1 == p3}")
 
    print(f"id(p1) = {id(p1)}")
    print(f"id(p2) = {id(p2)}")
    print(f"id(p3) = {id(p3)}")
 
    print(f"hash(p1): {hash(p1)}")
    print(f"hash(p2): {hash(p2)}")
    print(f"hash(p3): {hash(p3)}")
 
    point_dictionary = {
        p1 : "Point 1",
        p2 : "Point 2",
        p3 : "Point 3"
    }
 
    print(point_dictionary)
 
if __name__ == "__main__":
    main()