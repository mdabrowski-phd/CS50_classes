def main():
    text = input("camelCase:  ")

    for c in text:
        if c.isupper():
            print(f"_{c.lower()}", end="")
        else:
            print(c, end="")

    print()


if __name__ == "__main__":
    main()
