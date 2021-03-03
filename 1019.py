duration = int(input())

hours = (duration//60)//60
minutes = (duration//60)%60
seconds = duration%60

print("%d:%d:%d" % (hours, minutes, seconds))
