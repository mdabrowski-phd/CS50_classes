import validators


def main():
    print(validate(input("What's your email address? ")))


def validate(address):
    return "Valid" if validators.email(address) else "Invalid"


if __name__ == "__main__":
    main()
