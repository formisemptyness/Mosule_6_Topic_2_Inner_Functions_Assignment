'''
Program: inner_functions_assignment.py
Author: Joshua M. McGinley
Date: 10/5/2022
Create a python file inner_functions_assignment.py. In your inner_functions_assignment.py, write a function
measurements that accepts a list of measurements for a rectangle and returns a string with perimeter and area

    Write 2 inner functions that accept a list as parameter
        area(a_list) -- calculates the area
            recall accessing items in a list: a_list[#]
        perimeter(a_list) -- calculates the perimeter
            recall accessing items in a list: a_list[#]
    The outer, measurements function will call the area() and the perimeter()
    The outer function will build a string and return the following string:
        Perimeter = 11.0 Area = 7.14  # if this is the perimeter and the area.

    Next, add necessary statements to calculate for a square the perimeter and the area.
        len(a_list) is helpful to decide if the list has 1 or 2 items.
    In your main, call the function for a square and for a rectangle
'''

def measurements(a_list):
    def area(a_list):
        if len(a_list) > 1:
            theArea = a_list[0] * a_list[1]
        else:
            theArea = a_list[0] * a_list[0]
        #print(theArea)
        return theArea
    #area(a_list)
    def perimeter(a_list):
        if len(a_list) > 1:
            thePerimeter = (a_list[0] * 2) + (a_list[1] * 2)
        else:
            thePerimeter = a_list[0] * 4
        return thePerimeter
    #perimeter(a_list)
    #theArea = area(a_list)
    #thePerimeter = perimeter(a_list)
    perimArea = f'Perimeter = {perimeter(a_list)} Area = {area(a_list)}'
    return perimArea

if __name__ == '__main__':
    rectangle = [2.1, 3.4]
    result = measurements(rectangle)
    print(result)
    square = [3.5]
    result = measurements(square)
    print(result)


