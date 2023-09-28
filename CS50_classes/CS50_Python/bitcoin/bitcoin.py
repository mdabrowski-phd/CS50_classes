import sys, requests


def main():

    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    else:
        try:
            response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
            ammount = float(sys.argv[1]) * float(response["bpi"]["USD"]["rate_float"])
            print(f"${ammount:,.4f}")

        except ValueError:
            sys.exit("Command-line argument is not a number")

        except requests.RequestException:
            pass


main()
