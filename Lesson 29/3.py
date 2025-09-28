
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
p1 = Point(3, 4)
print(p1)  # Output: Point(3, 4)