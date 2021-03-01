from math import pow

a,b,c = [float(x) for x in input().split()]

rectangledTriangleAC = (a*c)/2
circleAreaRadiusC = pow(c,2) * 3.14159
trapeziumBaseABHeightC = ((a+b) * c)/2
squareAreaB = pow(b,2)
reactangleAreaAB = a * b

print("TRIANGULO: %.3f" % rectangledTriangleAC)
print("CIRCULO: %.3f" % circleAreaRadiusC)
print("TRAPEZIO: %.3f" % trapeziumBaseABHeightC)
print("QUADRADO: %.3f" % squareAreaB)
print("RETANGULO: %.3f" % reactangleAreaAB)
