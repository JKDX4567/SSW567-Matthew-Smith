import triangle_Classification #from  SSW567HW00B 
import math
def test_classify_triangle_e():
    assert triangle_Classification.classify_triangle(5,5,5) == "Equilateral Triangle"
    assert triangle_Classification.classify_triangle(7.5,7.5,7.5) == "Equilateral Triangle"
    #Here to test if it gets equilateral triangles right
def test_classify_triangle_rs():
    assert triangle_Classification.classify_triangle(5,4,3) == "Right Scalene Triangle"
    assert triangle_Classification.classify_triangle(13,12,5) == "Right Scalene Triangle"
    #Here to test if it gets right scalene triangles right
def test_classify_triangle_s():
    assert triangle_Classification.classify_triangle(5,4,7) == "Scalene Triangle"
    assert triangle_Classification.classify_triangle(6.5,4.32,9.1) == "Scalene Triangle"
    #Here to test if it gets scalene triangles right
def test_classify_triangle_i():
    assert triangle_Classification.classify_triangle(5,4,4) == "Isosceles Triangle"
    assert triangle_Classification.classify_triangle(10.72,10.72,9.3) == "Isosceles Triangle"
    #Here to test if it gets isosceles triangles right
def test_classify_triangle_ri():
    assert triangle_Classification.classify_triangle(3,3,3*math.sqrt(2)) == "Right Isosceles Triangle"
    #Here to test if it gets right isosceles triangles right
def test_classify_triangle_non_number():
    assert triangle_Classification.classify_triangle(3,3,"dummy") == "Not given a number for at least one input"
    assert triangle_Classification.classify_triangle(True,3,4) == "Not given a number for at least one input"
    #Here to test if it gets the right output assuming its not even given a number
def test_classify_triangle_invalid():
    assert triangle_Classification.classify_triangle(0,3,4) == "Invalid triangle, not possible given side lengths"
    assert triangle_Classification.classify_triangle(3,-1,5) == "Invalid triangle, not possible given side lengths"
    assert triangle_Classification.classify_triangle(3,4,50) == "Invalid triangle, not possible given side lengths"
    #Here to test if it gets the right output assuming its given numbers but they cant possibly form a triangle