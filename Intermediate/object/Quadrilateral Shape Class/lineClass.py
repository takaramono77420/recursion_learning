class Line:
    def __init__(self, startPoint, endPoint):
        self.startPoint = startPoint
        self.endPoint = endPoint
    
    def getLength(self):
        return int(((self.startPoint.x - self.endPoint.x)**2 + (self.startPoint.y - self.endPoint.y)**2)**(1/2))
    
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

a = Point(3,1)

b = Point(3,6)

lineAB = Line(a, b)

print(lineAB.getLength())

c = Point(1,3)

d = Point(6,15)

lineCD = Line(c, d)

print(lineCD.getLength()) 
