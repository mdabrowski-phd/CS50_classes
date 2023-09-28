import sys


def main():

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if not sys.argv[1].endswith('.py'):
            sys.exit("Not a Python file")

        else:
            try:
                with open(sys.argv[1]) as f:
                    lines = f.readlines()

                counter = 0
                for line in lines:
                    if not (line.lstrip().startswith("#") or line.lstrip() == ""):
                        counter += 1

                print(counter)

            except FileNotFoundError:
                sys.exit("File does not exist")


if __name__ == "__main__":
    main()
