def main():

    text = input("Input: ")
    print(f"Output: {shorten(text)}")


def shorten(word):

    text = []

    for c in word:
        if c in ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]:
            continue
        else:
            text.append(c)

    return "".join(text)


if __name__ == "__main__":
    main()
