import math

class Point:

    def __init__(self, x:int, y:int):

        self.x = x
        self.y = y


class LineSegment:

    def __init__(self, point1, point2):

        self.startpoint = point1
        self.endpoint = point2

    def slope(self):
        
        return (self.endpoint.y - self.startpoint.y) / (self.endpoint.x - self.startpoint.x)


    def length(self):
       
        return math.sqrt((self.endpoint.x - self.startpoint.x) ** 2 + (self.endpoint.y - self.startpoint.y) ** 2)    

"""
>>> from exercise05 import LineSegment
>>> from exercise05 import Point
>>> segment=LineSegment(Point(1,1), Point(3,2))
>>> segment.slope()
0.5
>>> segment.length()
2.23606797749979"""