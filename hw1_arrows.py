from visual import *

a = vector(0.3, 0.2, 0.5)
b = vector(0.1, 0.5, -0.2)
s = 1.8
print(a+b, a-b, s*a, cross(a, b), dot(a, b))

f = arrow(pos = vector(0, 0, 0), axis = vector(a+b), color = color.red)
g = arrow(pos = vector(0, 0, 0), axis = vector(a-b), color = color.blue)
i = arrow(pos = vector(0, 0, 0), axis = vector(cross(a, b)), color = color.green)

x = arrow(pos = vector(0, 0, 0), axis = vector(1, 0, 0), color = color.yellow)
y = arrow(pos = vector(0, 0, 0), axis = vector(0, 1, 0), color = color.yellow)
z = arrow(pos = vector(0, 0, 0), axis = vector(0, 0, 1), color = color.yellow)
