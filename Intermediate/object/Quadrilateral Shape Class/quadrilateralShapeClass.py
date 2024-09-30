import math
    
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, startPoint, endPoint):
        self.startPoint = startPoint
        self.endPoint = endPoint
    
    def getLength(self):
        return math.sqrt((self.startPoint.x - self.endPoint.x)**2 + (self.startPoint.y - self.endPoint.y)**2)

class QuadrilateralShape:
    def __init__(self, lineAB, lineBC, lineCD, lineDA):
        self.lineAB = lineAB
        self.lineBC = lineBC
        self.lineCD = lineCD
        self.lineDA = lineDA
    
    def getPerimeter(self):
        return int(self.lineAB.getLength() + self.lineBC.getLength() + self.lineCD.getLength() + self.lineDA.getLength())
    
    def getArea(self):
        x1, y1 = self.lineAB.startPoint.x, self.lineAB.startPoint.y
        x2, y2 = self.lineBC.startPoint.x, self.lineBC.startPoint.y
        x3, y3 = self.lineCD.startPoint.x, self.lineCD.startPoint.y
        x4, y4 = self.lineDA.startPoint.x, self.lineDA.startPoint.y
        area = 0.5 * abs(x1*y2 + x2*y3 + x3*y4 + x4*y1 - y1*x2 - y2*x3 - y3*x4 - y4*x1)
        return int(area)        

lineA = Line(Point(4,12), Point(0,6))

lineB = Line(Point(0,6), Point(4,0))

lineC = Line(Point(4,0), Point(8,6))

lineD = Line(Point(8,6), Point(4,12))
rhombus = QuadrilateralShape(lineA,lineB,lineC,lineD)
print(rhombus.getPerimeter())
print(rhombus.getArea())

lineE = Line(Point(0,0), Point(2,2))

lineF = Line(Point(2,2),  Point(2,6))

lineG = Line(Point(2,6),  Point(0,4))

lineH = Line(Point(0,4),  Point(0,0))

parallelogram = QuadrilateralShape(lineE,lineF,lineG,lineH)

print(parallelogram.getPerimeter())

print(parallelogram.getArea())

lineI = Line(Point(0,0), Point(4,0))

LineJ = Line(Point(4,0), Point(6,2))

lineK =  Line( Point(6,2),  Point(6,6))

lineL =  Line( Point(6,6),  Point(0,0))

trapezoid =  QuadrilateralShape(lineI,LineJ,lineK,lineL)

print(trapezoid.getPerimeter())

print(trapezoid.getArea())

lineM =  Line( Point(0,4),  Point(4,10))

lineN =  Line( Point(4,10),  Point(8,4))

lineO =  Line( Point(8,4),  Point(4,0))

lineP =  Line( Point(4,0),  Point(0,4))

kite =  QuadrilateralShape(lineM,lineN,lineO,lineP)

print(kite.getPerimeter())

print(kite.getArea())
lineQ =  Line( Point(0,0),  Point(8,0))

lineR =  Line( Point(8,0),  Point(10,12))

lineS =  Line( Point(10,12),  Point(2,6))

lineT =  Line( Point(2,6),  Point(0,0))

other =  QuadrilateralShape(lineQ,lineR,lineS,lineT)

print(other.getPerimeter())

print(other.getArea())