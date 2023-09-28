import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    m = re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)
    try:
        for group in m.groups():
            if int(group) < 0 or int(group) > 255:
                return False

    except:
        return False
    else:
        return True


if __name__ == "__main__":
    main()
