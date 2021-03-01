a,b,c = [int(x) for x in input().split()]

greaterAB = (a+b+abs((a-b)))/2
greaterABC = (greaterAB+c+abs((greaterAB-c)))/2

print("%d eh o maior" % greaterABC)
