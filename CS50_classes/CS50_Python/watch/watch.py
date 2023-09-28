import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        m = re.search(r"src=\"http(s)?://(www\.)?youtube\.com/embed/([a-zA-Z0-9]+)", s)
        return f"https://youtu.be/{m.group(3)}"
    except:
        return None


if __name__ == "__main__":
    main()