a,b,c = [float(x) for x in input().split()]

if((a == 0) or ((b ** 2) - 4 * (a * c)) < 0):
  print("Impossivel calcular")
else:
  r1 = (-b + ((b ** 2) - 4 * (a * c)) ** (0.5)) / (2 * a)
  r2 = (-b - ((b ** 2) - 4 * (a * c)) ** (0.5)) / (2 * a)

  print("R1 = %.5f" % r1)
  print("R2 = %.5f" % r2)
  