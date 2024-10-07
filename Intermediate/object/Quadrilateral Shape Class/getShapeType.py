
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
    
    def getSlope(self):

        if self.startPoint.x == self.endPoint.x:
            return float('inf') 
        return (self.startPoint.y - self.endPoint.y) / (self.startPoint.x - self.endPoint.x)

    def findTheLinearFunction(self):

        slope = self.getSlope()
        
        intercept = self.startPoint.y - slope * self.startPoint.x

        return lambda x : slope * x + intercept

    def onTheSameLine(self, point):

        fn = self.findTheLinearFunction()
        
        return fn(point.x) == point.y

def judgeNotQuadrilateral(lineAB, lineCD, lineBC):
    
    return lineAB.onTheSameLine(lineCD.startPoint) or lineAB.onTheSameLine(lineCD.endPoint) \
        or lineCD.onTheSameLine(lineAB.startPoint) or lineCD.onTheSameLine(lineAB.endPoint) \
        or lineBC.onTheSameLine(lineAB.startPoint) or lineBC.onTheSameLine(lineCD.endPoint)

def judgeTrapeziumHelper(a, c, b, d):

    x1=c.x-a.x
    x2=b.x-d.x
    x3=c.y-a.y
    x4=b.y-d.y
    d=float(x1*x4-x2*x3)
    if d==0: return False
    b1=b.x-a.x
    b2=b.y-a.y
    s=(b1*x4-b2*x2)/d
    t=(b2*x1-b1*x3)/d
    if 0<=s<=1 and 0<=t<=1: return True
    return False


def getShapeType(ax,ay,bx,by,cx,cy,dx,dy):
    # 関数を完成させてください
    a = Point(ax, ay)
    b = Point(bx, by)
    c = Point(cx, cy)
    d = Point(dx, dy)

    lineAB = Line(a, b)
    lineBC = Line(b, c)
    lineCD = Line(c, d)
    lineDA = Line(d, a)
    diagonaAC = Line(a, c)
    diagonaBD = Line(b, d)

    bd = diagonaBD.getLength()
    ac = diagonaAC.getLength()
    ab = lineAB.getLength()
    bc = lineBC.getLength()
    cd = lineCD.getLength()
    da = lineDA.getLength()

    slopeAB = lineAB.getSlope()
    slopeBC = lineBC.getSlope()
    slopeCD = lineCD.getSlope()
    slopeDA = lineDA.getSlope()

    if judgeNotQuadrilateral(lineAB, lineCD, lineBC):
        return "not a quadrilateral"

    if slopeAB == slopeCD and slopeBC == slopeDA:
        if ac != bd:
            if ab == bc:
                return "rhombus（ひし形）"
            else:
                return "parallelogram（平行四辺形）"
        else:
            if ab == bc:
                return "square（正方形）"
            else:
                return "rectangle（長方形）"
    elif (slopeAB == slopeCD or slopeBC == slopeDA) and judgeTrapeziumHelper(a, c, b, d):
        return "trapezoid（台形）"
    elif (lineAB.getLength() == lineBC.getLength() and lineCD.getLength() == lineDA.getLength()) \
        or (lineBC.getLength() == lineCD.getLength() and lineDA.getLength() == lineAB.getLength()):
        return "kite（凧）"
    else:
        return "other（その他）"




    




    
    





