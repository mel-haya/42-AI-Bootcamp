import string

def count(*args):
    if len(args) > 1:
        print("ERROR")
        exit()
    if len(args) == 0:
        text = input("please insert a text :\n")
        count(text)
    elif len(args) == 1:
        upper = 0
        lower = 0
        spaces = 0
        punctuation = 0
        for i in args[0]:
            if i.isupper():
                upper+=1
            elif i.
            

