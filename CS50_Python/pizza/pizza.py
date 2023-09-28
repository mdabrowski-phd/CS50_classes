import sys, csv
from tabulate import tabulate


def main():

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if not sys.argv[1].endswith('.csv'):
            sys.exit("Not a CSV file")

        else:
            try:
                with open(sys.argv[1]) as f:
                    reader = csv.reader(f)

                    items = []
                    for row in reader:
                        items.append(row)

                print(tabulate(items[1:], items[0], tablefmt="grid"))

            except FileNotFoundError:
                sys.exit("File does not exist")


if __name__ == "__main__":
    main()
