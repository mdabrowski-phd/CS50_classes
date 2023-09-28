import inflect


def main():

    names = []
    p = inflect.engine()

    while True:

        try:
            name = input("Name: ")
            names.append(name)

        except EOFError:

            print(f"Adieu, adieu, to {p.join(names)}")
            return

main()
