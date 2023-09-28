import random


while True:
    try:
        level = int(input("Level: "))

        if level > 0:
            break

    except:
        pass

n = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))

        if guess != 0:

            if guess > n:
                print("Too large!")

            elif guess < n:
                print("Too small!")

            else:
                print("Just right!")
                break

    except:
        pass
