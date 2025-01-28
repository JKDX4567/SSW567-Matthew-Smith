from SSW567.SSW567HW00B import SSW567HW00B_Triangles
import math
def test_classify_triangle():
    assert SSW567HW00B_Triangles.classify_triangle(5,5,5) == "equilateral"
    assert SSW567HW00B_Triangles.classify_triangle(5,4,3) == "right scalene"
    assert SSW567HW00B_Triangles.classify_triangle(5,4,7) == "scalene"
    assert SSW567HW00B_Triangles.classify_triangle(5,4,4) == "isosceles"
    assert SSW567HW00B_Triangles.classify_triangle(3,3,3*math.sqrt(2)) == "right isosceles"