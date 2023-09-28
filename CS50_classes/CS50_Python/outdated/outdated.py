MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    total = 0

    while True:

        try:
            date = input("Date: ").strip()
            m, d, y = date.split('/')

            if int(d) <= 31 and int(m) <= 12:
                print(f"{y}-{int(m):02}-{int(d):02}")
                return

        except:

            try:
               md, y = date.split(', ')
               m, d = md.split()

               if int(d) <= 31:
                   print(f"{y}-{(MONTHS.index(m) + 1):02}-{int(d):02}")
                   return

            except:
                pass


main()
