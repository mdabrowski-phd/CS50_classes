def main():
    expression = input("Expression: ")
    x, y, z = expression.split()

    match(y):
        case "+":
            print(round(float(x) + float(z), 1))
        case "-":
            print(round(float(x) - float(z), 1))
        case "*":
            print(round(float(x) * float(z), 1))
        case "/":
            print(round(float(x) / float(z), 1))


main()
