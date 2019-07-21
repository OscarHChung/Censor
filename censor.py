from cs50 import get_string
from sys import argv

words = set()

def main():

    if len(argv) != 2:
        print("Usage: python censor.py dictionary")
        exit(1)

    load(argv[1])
    input = get_string("What messasge would you like to censor? ")
    tokens = input.split()
    limit = 0

    for i in tokens:
        if check(i):
            for j in i:
                print("*", end="")
        else:
            print(i, end="")

        limit = limit + 1

        if limit != len(tokens):
            print(" ", end="")

    print("\n")
    return True

def load(banned):
    file = open(banned, "r")
    for line in file:
        words.add(line.rstrip("\n"))
    file.close()
    return True

def check(word):
    return word.lower() in words


if __name__ == "__main__":
    main()
