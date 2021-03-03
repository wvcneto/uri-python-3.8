value = int(input())
amount = value

print(amount)

hundred = (amount//100)
amount -= (hundred*100)

fifty = (amount//50)
amount -= (fifty*50)

twenty = (amount//20)
amount -= (twenty*20)

ten = (amount//10)
amount -= (ten*10)

five = (amount//5)
amount -= (five*5)

two = (amount//2)
amount -= (two*2)

print("%d nota(s) de R$ 100,00" % hundred)
print("%d nota(s) de R$ 50,00" % fifty)
print("%d nota(s) de R$ 20,00" % twenty)
print("%d nota(s) de R$ 10,00" % ten)
print("%d nota(s) de R$ 5,00" % five)
print("%d nota(s) de R$ 2,00" % two)
print("%d nota(s) de R$ 1,00" % amount)
