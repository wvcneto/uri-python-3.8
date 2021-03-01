total = 0
for n in range(2):
    cod,quantity,price = input().split()
    
    total += int(quantity) * float(price)
print("VALOR A PAGAR: R$ %.2f" % total)
