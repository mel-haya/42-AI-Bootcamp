import sys

if len(sys.argv) != 3 or not isinstance(sys.argv[1], str) or not sys.argv[2].isdigit():
    print("ERROR")
    exit()
words = sys.argv[1].split(" ")

words = list(filter(lambda w: len(w) >= int(sys.argv[2]), words))

print(words)
