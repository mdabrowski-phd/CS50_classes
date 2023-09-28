def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if len(s) > 6 or len(s) < 2:
        return False
    elif not s[:2].isalpha():
        return False
    elif not s.isalnum():
        return False
    else:

        for i in range(len(s) - 1):
            if s[i].isdigit() and s[i+1].isalpha():
                return False
            if s[i].isalpha() and s[i+1] == '0':
                return False

    return True


main()
