import random


def main():

    score = 0
    level = get_level()

    for i in range(10):

        answer = ask_question(level)
        if answer:
            score += 1

    print(f"Score: {score}")


def get_level():

    while True:
        try:
            level = int(input("Level: "))

            if level in [1, 2, 3]:
                return level

        except:
            pass


def generate_integer(level):

    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError


def ask_question(level):

    X, Y = generate_integer(level), generate_integer(level)

    for _ in range(3):

        try:
            print(f"{X} + {Y} = ", end="")
            Z = int(input())

            if Z == X + Y:
                return True
            else:
                print("EEE")

        except:
            print("EEE")

    print(f"{X} + {Y} = {X + Y}")
    return False


if __name__ == "__main__":
    main()
