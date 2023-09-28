def main():

    while True:
        answer = input("Fraction: ")

        try:
            percentage = convert(answer)
            break

        except (ValueError, ZeroDivisionError):
            continue

    print(gauge(percentage))


def convert(fraction):

    x, y = fraction.split('/')

    if x.isdigit() is False or y.isdigit() is False or int(x) > int(y):
        raise ValueError
    elif int(y) == 0:
        raise ZeroDivisionError
    else:
        return round(100 * int(x) / int(y))


def gauge(percentage):

    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()



