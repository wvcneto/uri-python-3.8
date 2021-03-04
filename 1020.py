timeInDays = int(input())

years = timeInDays//365

months = (timeInDays%365)//30

days = (timeInDays%365)%30

print("%d ano(s)" % years)
print("%d mes(es)" % months)
print("%d dia(s)" % days)
