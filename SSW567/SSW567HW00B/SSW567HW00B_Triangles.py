import math

def classify_triangle(x,y,z):
    #x,y,z are sides 1,2 and 3 respecitively
    theTriangle = ""
    #here so that I can combine the "right" classifcation with one of the other types
    '''
    print(x**2)
    print(y**2)
    print(z**2)
    these are here for initial testing
    '''
    if (round(x**2, 5) + round(y**2, 5) == round(z**2, 5)) or (round(x**2, 5) + round(z**2, 5) == round(y**2, 5)) or (round(z**2, 5) + round(y**2, 5) == round(x**2, 5)):
        theTriangle = theTriangle + "right " 
    #Rounding because right isosceles triangles do exist, but if use just pi or square roots, youll often be "off" just due to how python handles it
    #So I have it round to 5 decimal places, since for most purposes thats good enough while getting rid of the error, and thus allowing for right isosceles triangles
    if x==y==z:
        theTriangle = theTriangle + "equilateral"
    elif x==y or x==z or y==z:
        theTriangle = theTriangle + "isosceles"
    
    else:
        theTriangle = theTriangle + "scalene"
    return theTriangle
#print (classify_triangle(5,5,5))
#print (classify_triangle(5,4,3))
#print (classify_triangle(5,4,7))
#print (classify_triangle(5,4,4))
#print (classify_triangle(3,3,3*math.sqrt(2)))
