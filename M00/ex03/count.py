import string

def text_analyzer(*args):
    '''This function counts the number of upper characters, lower characters,
punctuation and spaces in a given text'''
    if len(args) > 1:
        print("ERROR")
        return()
    if len(args) == 0:
        text = input("please insert a text :\n")
        text_analyzer(text)
    elif len(args) == 1:
        upper = 0
        lower = 0
        spaces = 0
        punctuation = 0

        for i in args[0]:
            if i.isupper():
                upper+=1
            elif i.islower():
                lower+=1
            elif i == ' ':
                spaces+=1
            elif i in string.punctuation:
                punctuation += 1
        print("The text contains " ,len(args[0])," characters:")
        print("- ", upper," upper letters")
        print("- ", lower," lower letters")
        print("- ", punctuation," punctuation marks")
        print("- ", spaces," spaces")


            

