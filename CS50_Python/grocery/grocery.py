def main():

    items = {}

    while True:

        try:
            item = input().upper()
            items[item] = items.get(item, 0) + 1

        except EOFError:
            print()
            break

        except KeyError:
            pass

    for item in sorted(items):
        print(f"{items[item]} {item}")


main()