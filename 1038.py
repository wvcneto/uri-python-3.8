code,count = [int(v) for v in input().split()]

total = 0

if(code == 1):
    total = count * 4.0
elif(code == 2):
    total = count * 4.50
elif(code == 3):
    total = count * 5.00
elif(code == 4):
    total = count * 2.00
elif(code == 5):
    total = count * 1.50


print("Total: R$ %.2f" % total)
