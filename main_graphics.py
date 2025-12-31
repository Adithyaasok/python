
from graphics import rectangle, circle
from graphics.three_d import cuboid, sphere

print("Area of rectangle:", rectangle.area(5,3))
print("Perimeter of rectangle:", rectangle.perimeter(5,3))
print("Area of circle:", circle.area(4))
print("Perimeter of circle:", circle.perimeter(4))
print("Surface area of cuboid:", cuboid.surface_area(3,2,4))
print("Volume of cuboid:", cuboid.volume(3,2,4))
print("Surface area of sphere:", sphere.surface_area(2))
print("Volume of sphere:", sphere.volume(2))
