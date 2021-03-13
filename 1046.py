initial, final = [int(hours) for hours in input().split()]

if initial < final:
    total = final - initial
else:
    total = (24 - initial) + final

print("O JOGO DUROU %d HORA(S)" % total)
