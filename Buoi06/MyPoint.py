from math import sqrt
class MyPoint:
    # Gắn giá trị default cho 2 field tọa độ
    x = 0
    y = 0
    
    #  Định nghĩa hàm đặt giá trị tọa độ
    def set_location(self, xx, yy):
        self.x = xx
        self.y = yy
        
    def __init__(self, x, y):
        self.x = x
        self.y = y

        
    # Định nghĩa hàm tính khoảng cách tới gốc tọa độ O(0,0)
    def distance_from_origin(self):
        return sqrt(self.x * self.x + self.y * self.y)


    # Định nghĩa hàm tính khoảng cách giữa 2 điểm
    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx * dx + dy * dy)


    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"


if __name__ == "__main__":
    # Create a new Point object
    p1 = MyPoint(2, 3)
    print(p1) # Output: Point(2, 3)

    # Move the point
    p1.move(1, -1)
    print(p1) # Output: Point(3, 2)