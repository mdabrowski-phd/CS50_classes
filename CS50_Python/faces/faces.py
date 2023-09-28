def main():
    text = input("Input:  ")
    print(f"Output: {faces(text)}")

def faces(input):
    return input.replace(":)", "🙂").replace(":(", "🙁")


main()
