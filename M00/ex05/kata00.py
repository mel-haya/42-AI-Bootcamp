t = (19,42,21,5,99,8,11)
i = 0
s = "The " + str(len(t)) + " numbers are:"
while i < len(t):
    s += " " + str(t[i])
    if i != len(t) - 1:
        s += ","
    i+=1

print(s)