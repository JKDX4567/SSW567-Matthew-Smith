import math
import numbers

def classify_triangle(x,y,z):
    #x,y,z are sides 1,2 and 3 respecitively
    if isinstance(x, (int,float)) and isinstance(y, (int,float)) and isinstance(z, (int,float)) and not isinstance(x, bool) and not isinstance(z, bool) and not isinstance(y, bool):
    #Makes sure we are given numbers and not something unusable/ Not valid (needed to seperate variables because otherwise didnt work properly)
        if (x and y and z) > 0 and x + y > z and x + z > y and y + z > x:
        # Makes sure we are given a triangle that is even possible (assumes we have valid numbers)
            theTriangle = ""
            #here so that I can combine the "right" classifcation with one of the other types
            '''
            print(x**2)
            print(y**2)
            print(z**2)
            these are here for initial testing
            '''
            if (round(x**2, 5) + round(y**2, 5) == round(z**2, 5)) or (round(x**2, 5) + round(z**2, 5) == round(y**2, 5)) or (round(z**2, 5) + round(y**2, 5) == round(x**2, 5)):
                theTriangle = theTriangle + "Right " 
            #Rounding because right isosceles triangles do exist, but if use just pi or square roots, youll often be "off" just due to how python handles it
            #So I have it round to 5 decimal places, since for most purposes thats good enough while getting rid of the error, and thus allowing for right isosceles triangles
            if x==y==z:
                theTriangle = theTriangle + "Equilateral"
            elif x==y or x==z or y==z:
                theTriangle = theTriangle + "Isosceles"
            
            else:
                theTriangle = theTriangle + "Scalene"
            return theTriangle + " Triangle"
        else:
            return "Invalid triangle, not possible given side lengths"
    else:
        return "Not given a number for at least one input"
print (classify_triangle(5,5,5))
print (classify_triangle(5,4,3))
print (classify_triangle(5,4,7))
print (classify_triangle(5,4,4))
print (classify_triangle(3,3,3*math.sqrt(2)))
print (classify_triangle(3,3,"duh"))
print (classify_triangle(3,3,15))
print (classify_triangle(3,3,-5))
print (classify_triangle(3,3,0))
print (classify_triangle(2,False,4))