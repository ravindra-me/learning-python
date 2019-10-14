r=3
n=3
def area_of_polygon_inside_circle(r, n):
    from math import sin 
    A = ((r * r * n) * sin((360 / n) *(3.14159 / 180)) / 2)
				
    return round(A,3) 
print(area_of_polygon_inside_circle(r,n))
  