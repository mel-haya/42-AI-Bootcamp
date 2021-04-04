t = ( 0, 4, 132.42222, 10000, 12345.67)

s = "Module_" + format(t[0],'02d') + ", "
s += "ex_" + format(t[1],'02d') + ", "
s += format(t[2],'.2f') + ", "
s += format(t[3],'.2e') + ", "
s += format(t[4],'.2e')

print (s)