import sys, csv

def main():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    else:
        try:
            with open(sys.argv[1], "r") as f:
                reader = csv.DictReader(f)

                students = []
                for row in reader:
                    students.append({"first": row["name"].split(",")[1].lstrip(), "last": row["name"].split(",")[0], "house": row["house"]})

            with open(sys.argv[2], "w") as f:
                writer = csv.DictWriter(f, fieldnames=["first", "last", "house"])
                writer.writeheader()

                for student in students:
                    writer.writerow(student)

        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")


if __name__ == "__main__":
    main()
