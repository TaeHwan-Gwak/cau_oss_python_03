import math

class line:

    __width = 0
    __height = 0
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def set_length(self, width, height):
        self.__width = width
        self.__height = height

    def get_length(self):
        return self.__width, self.__height

    def area_rectangle(width, height):
        if width <= 0 or height <=0: raise ValueError
        return width * height

    def area_ellipse(width, height):
        if width <= 0 or height <=0: raise ValueError
        return width * height * math.pi

    def area_right_triangle(width, height):
        if width <= 0 or height <=0: raise ValueError
        return width * height / 2

    # def area_square(length):
    #    return length * length

    # def area_circle(length):
    #    return length * length * math.pi

    # def area_regular_triangle(length):
    #    return length * length * math.sqrt(3) / 4
