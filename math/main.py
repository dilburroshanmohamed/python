from basic_operations import arithmatic //file should be same
from geomatric_operations import area //file should be same

print("Arithmetic Operations")
print("5 + 3 =",arithmatic.add(5,3))
print("5 - 3 =",arithmatic.subtract(5,3))
print("5 * 3 =",arithmatic.multiply(5,3))
print("5 / 3 =",arithmatic.divide(5,3))
print("5 / 0 =",arithmatic.divide(5,0))


print("Area operations")
print("rectangle area: ",area.rect_area(5,3))
print("circle area: ",area.circle_area(7))
print("traiangle area: ",area.triangle_area(4,5))
