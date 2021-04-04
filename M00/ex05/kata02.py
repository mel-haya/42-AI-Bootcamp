t = (3,30,2019,9,25)
p = {3:'/',4:'/',2:' ',0:':',1:''}
time = ""

for key in p:
    time += format(t[key],'02') + p[key]

print(time)