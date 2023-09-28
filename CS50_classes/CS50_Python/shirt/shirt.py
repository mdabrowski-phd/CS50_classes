import sys, os
from PIL import Image, ImageOps


def main():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    ext1 = os.path.splitext(sys.argv[1])[1].lower()
    ext2 = os.path.splitext(sys.argv[2])[1].lower()

    if ext1 not in [".jpg", ".jpeg", ".png"]:
        sys.exit("Invalid input")

    if ext1 != ext2:
        sys.exit("Input and output have different extensions")

    try:
        with Image.open(sys.argv[1]) as im:

            shirt = Image.open("shirt.png")
            im = ImageOps.fit(im, shirt.size)
            im.paste(shirt, shirt)
            im.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


if __name__ == "__main__":
    main()
