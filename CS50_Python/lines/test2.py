import sys, random
from pyfiglet import Figlet


def main():

    figlet = Figlet()
    fonts = figlet.getFonts()

    if len(sys.argv) == 1:

        text = input("Input: ")
        font = random.choice(fonts)
        figlet.setFont(font=font)

    elif len(sys.argv) == 3 and sys.argv[1] in ['-f', '--font'] and sys.argv[2] in fonts:

        text = input("Input: ")
        figlet.setFont(font=sys.argv[2])

    else:
        sys.exit("Invalid usage")

    print(f"Output:\n {figlet.renderText(text)}")


main()