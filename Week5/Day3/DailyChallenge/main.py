

#// My method that worked until PART 2 started, then followed Yossi's method.


#PART 1

# import math
# import turtle

# # # The goal is to create a class that represents a simple circle.
# # # A Circle can be defined by either specifying the radius or the diameter. 
# # # The user can query the circle for either its radius or diameter.


# class Circle():
#     def __init__(self, radius):
#         self.radius = radius
        
#     def diameter(self):
#         return self.radius*2
    
#     def area(self):
#         return self.radius**2*3.14
    
#     def perimeter(self):
#         return 2*self.radius*3.14

# NewCircle = Circle(4)


# # # Compute the circle’s area

# print(NewCircle.__dict__)
# print(NewCircle.radius)
# print(NewCircle.diameter())
# print(NewCircle.area())
# print(NewCircle.perimeter())



#// PART 2
# # # Print the circle and get something nice
# # # Be able to add two circles together
# # # Be able to compare two circles to see which is bigger
# # # Be able to compare two circles and see if there are equal
# # # Be able to put them in a list and sort them#

# NewCircle = repr(NewCircle)

# print(NewCircle.__str__)

# c1 = Circle(2)
# c2 = Circle(3)
# c3=c1+c2
# print(c3.radius)

# c1.__add__(self, c2)
# c1.__sub__(self, c2)
# c2.__mul__(self, 3)

# def__gt__(c1,c2)
# #False

# def__lt__(c1 ,c2)
# # True

# def__eq__ (c1 == c2)
# # False

# c3 = Circle(4)
# c2 == c3
# # True

# class Circle:
  
#     def __init__(self, val):
#         self.val = val

#     def sort_key(self):
#         return self.val
    
# val = Circle(Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1))

# def draw(self):
#         t = turtle.turtle()
#         t.circle(self.radius)
    

# t.circle(c1.radius)

#//  following yossi's method:

# import math
# import turtle

# class Circle:

#     def __init__(self, radius: int):
#         self.radius = radius
#         self.diameter = self.radius * 2

#     @classmethod
#     def from_diameter(cls, diameter: int):
#         return Circle(diameter // 2)

#     @staticmethod
#     def make_sentence(sentence):
#         print("CIRCLE said: ", sentence)

#     @property
#     def circle_area(self):
#         return math.pi * (self.radius ** 2)

#     def draw(self):
#         t = turtle.Turtle()
#         t.circle(self.radius)

#     def __add__(self, other_c):
#         return Circle(radius=self.radius + other_c.radius)

#     def __lt__(self, other_c):
#         return self.circle_area < other_c.circle_area

#     def __gt__(self, other_c):
#         return self.circle_area > other_c.circle_area

#     def __eq__(self, other_c):
#         return self.circle_area == other_c.circle_area

#     # user friendly
#     def __str__(self) -> str:
#         return str(self.radius)

#     # readable, but also applicable
#     def __repr__(self):
#         return str(self.radius)

# c1 = Circle(2)
# c2 = Circle.from_diameter(10)

# c3 = c1 + c2 
# c4 = Circle(radius=c3.radius)
# c5 = Circle(int(repr(c1)))

# circles = [c4, c2, c3, c1, c5]
# print(circles)

# circles.sort()
# print(circles)