def main():


    while True:

        try:
            x, y = input("Fraction: ").split('/')
            answer = int(x) / int(y)
            if answer > 1:
                pass
            elif answer >= 0.99:
                print("F")
                return
            elif answer <= 0.01:
                print("E")
                return
            else:
                print(f"{int(100 * round(answer, 2))}%")
                return

        except ValueError:
            pass
        except ZeroDivisionError:
            pass


main()
