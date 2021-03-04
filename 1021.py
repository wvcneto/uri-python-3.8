from math import modf

amount = float(input())

value = modf(amount)
notes = int(value[1])
value = str(value[0]).split('.')
cents = int(value[1][:2])

hundred = notes//100
notes = notes%100

fifty = notes//50
notes = notes%50

twenty = notes//20
notes = notes%20

ten = notes//10
notes = notes%10

five = notes//5
notes = notes%5

two = notes//2

one = notes%2

fiftyCents = cents//50
cents = cents%50

twentyFiveCents = cents//25
cents = cents%25

tenCents = cents//10
cents= cents%10

fiveCents = cents//5

oneCents = cents%5

print("NOTAS:")
print("%d nota(s) de R$ 100.00" % hundred)
print("%d nota(s) de R$ 50.00" % fifty)
print("%d nota(s) de R$ 20.00" % twenty)
print("%d nota(s) de R$ 10.00" % ten)
print("%d nota(s) de R$ 5.00" % five)
print("%d nota(s) de R$ 2.00" % two)

print("MOEDAS:")
print("%d moeda(s) de R$ 1.00" % one)
print("%d moeda(s) de R$ 0.50" % fiftyCents)
print("%d moeda(s) de R$ 0.25" % twentyFiveCents)
print("%d moeda(s) de R$ 0.10" % tenCents)
print("%d moeda(s) de R$ 0.05" % fiveCents)
print("%d moeda(s) de R$ 0.01" % oneCents)
