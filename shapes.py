import math





class Shape:
    def calculate_area(self):
        pass
    
    def calculate_perimeter(self):
        pass
    
    
class Rectangle(Shape):
    def __init__(self) :
        self.__height = 0
        self.__width = 0 
    def set_height(self,height):
        self.__height = height

    def set_width(self,width):
        self.__width = width

    def get_height(self):
        return self.__height
    def get_width(self):
        return self.__width
    

    def calculate_area(self):
        '''This method is used to calculate the area of the rectange'''
        return self.get_width()* self.get_height()
    
    def calculate_perimeter(self):
        '''This method is used to calculate the perimeter of the rectange'''
        return 2 * (self.get_width() + self.get_height())


class Triangle(Shape):
    def __init__(self, face1, face2, face3):
        self.face1 = face1
        self.face2 = face2
        self.face3 = face3

    def calculate_perimeter(self):
        '''This method is used to calculate the perimeter of the Triangle'''
        return self.face1 + self.face2 + self.face3

    def calculate_area(self):
        '''This method is used to calculate the area of the Triangle'''
        s = (self.face1 + self.face2 + self.face3) / 2
        return math.sqrt(s * (s - self.face1) * (s - self.face2) * (s - self.face3))


class Circle:
    #static method
    def calculate_perimeter(radius):
        '''This method is used to calculate the perimeter of the Circle'''
        return 2 * math.pi * radius

    def calculate_area(radius):
        '''This method is used to calculate the area of the circle'''

        return math.pi * radius ** 2



def main():
    print("Circle Perimeter:", Circle.calculate_perimeter(10))  
    print("Circle Area:", Circle.calculate_area(10)) 

    rectangle = Rectangle()
    rectangle.set_height(12)
    rectangle.set_width(24)
    
    print("Rectangle Perimeter:", rectangle.calculate_perimeter())  
    print("Rectangle Area:", rectangle.calculate_area())  
    
    triangle = Triangle(5, 8, 5)
    print("Triangle Perimeter:", triangle.calculate_perimeter()) 
    print("Triangle Area:", triangle.calculate_area()) 
    
    
    
main()
    
    