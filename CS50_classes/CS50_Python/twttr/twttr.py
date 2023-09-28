def main():
    text = input("Input: ")
    print("Output: ", end="")

    for c in text:
        if c in ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]:
            print("", end="")
        else:
            print(c, end="")

    print()


if __name__ == "__main__":
    main()
