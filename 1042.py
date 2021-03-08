v1,v2,v3 = [int(x) for x in input().split()]

if(v1 > v2 and v1 > v3):
    first = v1
    if(v2 > v3):
        second = v2
        third = v3
    else:
        second = v3
        third = v2
if(v2 > v1 and v2 > v3 ):
    first = v2
    if(v1 > v3):
        second = v1
        third = v3
    else:
        second = v3
        third = v1
if(v3 > v1 and v3 > v2):
    first = v3
    if(v1 > v2):
        second = v1
        third = v2
    else:
        second = v2
        third = v1

print(third)
print(second)
print(first)

print()

print(v1)
print(v2)
print(v3)
