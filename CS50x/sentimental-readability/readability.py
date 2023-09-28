from cs50 import get_string


def main():
    text = get_string("Text: ")

    L = count_letters(text) / count_words(text) * 100
    S = count_sentences(text) / count_words(text) * 100

    index = round(0.0588 * L - 0.296 * S - 15.8)

    if index >= 16:
        print("Grade 16+")
    elif index < 1:
        print("Before Grade 1")
    else:
        print("Grade", index)


def count_letters(text):
    counter = 0

    for c in text:
        if "A" <= c <= "Z" or "a" <= c <= "z":
            counter += 1

    return counter


def count_words(text):
    counter = 1

    for c in text:
        if c == " ":
            counter += 1

    return counter


def count_sentences(text):
    counter = 0

    for c in text:
        if c in [".", "!", "?"]:
            counter += 1

    return counter


if __name__ == "__main__":
    main()
