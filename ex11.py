from random import randint
n = randint(1,100)
m = 0
g = 0

while m != n:
    g = g + 1
    m = int(input("Your guess: "))
    if m < n:
        print("Your number is lower than the actual one.")
    elif m > n:
        print("Your number is higher than the actual one.")
    elif m == n:
        print(f"You guessed it! It took you {g} uesses to find it.")
        print(f"Your number of guesses: {g}")
