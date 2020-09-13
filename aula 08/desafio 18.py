import math

angle = int(input('Enter the value of the angle:'))
sine = math.sin(math.radians(angle))
cos = math.cos(math.radians(angle))
tan = math.tan(math.radians(angle))

print('The sine of the angle {} is {:.2f}'.format(angle, sine))
print('The cosine of the angle {} is {:.2f}'.format(angle,cos))
print('The tangent of the angle {} is {:.2f}'.format(angle, tan))