def main():

    answer = input("Greeting: ")
    print(f"${value(answer)}")


def value(greeting):

    answer = greeting.lower().strip()

    if answer.startswith("hello"):
        return 0
    else:
        if answer.startswith("h"):
            return 20
        else:
            return 100


if __name__ == "__main__":
    main()
