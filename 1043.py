a,b,c = [float(x) for x in input().split()]

if(a < (b + c) and b < (a + c) and c < (a + b)):
    perimetro = a + b + c
    print("Perimetro = %.1f" % perimetro)
else:
    area = c * (a + b)/2
    print("Area = %.1f" % area)
