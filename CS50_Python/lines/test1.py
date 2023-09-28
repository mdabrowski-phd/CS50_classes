def main():
    answer = input("Greeting: ").lower().strip()
    if answer.startswith("hello"):
        print("$0")
    else:
        if answer.startswith("h"):
            print("$20")
        else:
            print("$100")


main()