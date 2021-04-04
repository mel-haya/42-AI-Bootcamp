import random

secret = random.randint(1,99)

print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!")
try_count = 1
s = 0
while 1:
    print("What's your guess between 1 and 99?")
    i = input(">> ")
    if i == "exit":
        print("auf wiedersehen !!")
        exit()
    if not i.isdigit() :
        print("That's not a number")
    elif int(i) > secret:
        print("Too high!")
    elif int(i) < secret:
        print("Too low!")
    elif int(i) == secret:
        if int(i) == 42:
            print("The answer to the ultimate question of life, the universe and everything is 42.")
        if(try_count == 1):
            print("Congratulations! You got it on your first try!")
        else:
            print("Congratulations, you've got it!")
            print("You won in" , try_count , "attempts!")
        exit()
    try_count += 1


