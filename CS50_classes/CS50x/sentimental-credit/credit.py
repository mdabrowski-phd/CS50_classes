from cs50 import get_int


def main():
    number = get_card_number()
    check_validity(number)


def get_card_number():
    return get_int("Number: ")


def check_validity(number):
    checksum = calculate_checksum(number)

    if checksum % 10 == 0:
        length = calculate_length(number)

        if isAMEX(number, length):
            print("AMEX")

        elif isMASTERCARD(number, length):
            print("MASTERCARD")

        elif isVISA(number, length):
            print("VISA")
        else:
            print("INVALID")

    else:
        print("INVALID")


def calculate_length(number):
    numDigits = 0

    while number:
        numDigits += 1
        number //= 10

    return numDigits


def calculate_checksum(number):
    odd_sum, even_sum, idx = 0, 0, 0

    odd_sum += number % 10
    number //= 10
    idx += 1

    while number:
        if idx % 2 == 0:
            odd_sum += number % 10

        else:
            tmp = 2 * (number % 10)
            if tmp >= 10:
                even_sum += (tmp % 10) + 1
            else:
                even_sum += tmp

        number //= 10
        idx += 1

    return odd_sum + even_sum


def isAMEX(number, length):
    if length == 15:
        tmp = number // 10000000000000
        if tmp == 34 or tmp == 37:
            return True

    return False


def isMASTERCARD(number, length):
    if length == 16:
        tmp = number // 100000000000000
        if 51 <= tmp <= 55:
            return True

    return False


def isVISA(number, length):
    if length == 13:
        tmp = number // 1000000000000
        if tmp == 4:
            return True

    elif length == 16:
        tmp = number // 1000000000000000
        if tmp == 4:
            return True

    return False


if __name__ == "__main__":
    main()
