import sys
import time
from time import sleep

def up():
    sys.stdout.write('\x1b[1A')
    sys.stdout.flush()

def down():
    sys.stdout.write('\n')
    sys.stdout.flush()

def ft_progress(listy):
    t1 = time.perf_counter()
    t2 = 0
    eta = 0
    for i in listy:
        yield i
        i+=1
        if i == 2:
            res = ret * len(listy)
        eta = (t2 / (i + 1)) * len(listy)
        perc = int(i / len(listy) * 100)
        perc1 = "{:3d}".format(perc)
        equals = "%][{0}>".format("=" * int(perc / 5)) 
        spaces = "{0}]".format(" " * int(20 - int(perc / 5)))
        progress = " " + "{:4d}".format(i) + "/" + str(len(listy))
        elapsed = " | elapsed time " + "{:5.2f}".format(t2) +"s"
        print("\rETA: "+ "{:5.2f}".format(eta) +"s [" + perc1 + equals + spaces + progress + elapsed)
        
        print("...")
        print("🤷",end='')
        up();up()
        t2 = time.perf_counter() - t1
        if(i == len(listy)):
            down()
        

listy = range(3333)
ret = 0
for elem in ft_progress(listy):
    ret += elem
    sleep(0.005)
print()
print(ret)
