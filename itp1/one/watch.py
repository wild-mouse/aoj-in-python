import fileinput

s = int(input())

h = int(s / (60 * 60))
m = int((s % (60 * 60)) / 60)
sec = s % 60

print("{}:{}:{}".format(h, m, sec))
