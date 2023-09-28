from datetime import date
import sys, inflect


p = inflect.engine()


def main():


    try:
        year, month, day = input("Date of Birth: ").split("-")
        year, month, day = int(year), int(month), int(day)

    except ValueError:
        sys.exit("Invalid Date")

    print(convert(year, month, day))


def convert(year, month, day):

    diff = date.today() - date(year, month, day)
    minutes = diff.days * 24 * 60

    return f"{p.number_to_words(minutes, andword='')} minutes".capitalize()


if __name__ == "__main__":
    main()
