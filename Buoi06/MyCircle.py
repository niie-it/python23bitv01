# Định nghĩa lớp hình tròn Circle
import math
import turtle

class Circle:
    radius = 0
    color = ''
    x = 0
    y = 0

    def __init__(self, radius, color, x, y):
        self.radius = radius
        self.color = color
        self.x = x
        self.y = y

    def getRadius(self):
        return self.radius
   
    def getArea(self):
        return math.pi * self.radius ** 2

    def getPerimeter(self):
        """
        Phương thức tính chu vi đường tròn
        """
        return 2 * math.pi * self.radius

    def draw(self, t):
        """Phương thức vẽ đường tròn"""        
        t.hideturtle()
        t.color(self.color)
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        t.circle(self.radius)

    def __str__(self):
        return f"Circle {self.color} R = {self.radius}, S = {self.getArea()}"
       
# Demo
if __name__ == "__main__":
    print(turtle.screensize()) # (400, 300)
    t = turtle.Turtle()

    ht1 = Circle(77, 'blue', 100, 100)
    ht2 = Circle(9, 'black', 200, 200)
    print(ht1.radius, ht1.getRadius())
    print(ht2)
    ht1.draw(t)

    c = Circle(100, 'red', 250, -200)
    print(c)
    c.draw(t)
    print("S = ", c.getArea())
    print("C = ", c.getPerimeter())
