import sys
import time

def ft_progress(listy):
    t2 = 0
    shortest = 1
    longest = 0
    eta = 0
    for i in listy:
        yield i
        i+=1

        eta = (t2 / (i + 1)) * len(listy)
        perc = int(i / listy[-1] * 100)
        perc1 = "{:3d}".format(perc)
        equals = "%][{0}>".format("=" * int(perc / 5)) 
        spaces = "{0}]".format(" " * int(20 - int(perc / 5)))
        progress = " " + "{:4d}".format(i) + "/" + str(len(listy))
        elapsed = " | elapsed time " + "{:5.2f}".format(t2) +"s"
        sys.stdout.write("\rETA: "+ "{:7.2f}".format(eta) +"s [" + perc1 + equals + spaces + progress + elapsed + "")
        sys.stdout.flush()
        t2 = time.perf_counter()


listy = range(2000)
ret = 0
for elem in ft_progress(listy):
    ret += elem
    time.sleep(0.005)
print()
print(ret)




# for i in range(10):
#     sys.stdout.write("\r{0}>".format("="*i))
#     # 
#     time.sleep(1)