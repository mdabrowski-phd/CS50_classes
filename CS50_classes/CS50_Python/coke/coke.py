def main():
    amount_due = 50

    while amount_due > 0:

        amount = int(input("Insert Coin: "))
        if amount in [25, 10, 5]:
            amount_due -= amount
        if amount_due <= 0:
            print(f"Change Owed: {-amount_due}")
        else:
            print(f"Amount Due: {amount_due}")


if __name__ == "__main__":
    main()
