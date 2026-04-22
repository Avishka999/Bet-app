def deposit():
    while True:
        try:
            amount = float(input("Enter the amount to deposit: "))
            if amount <= 0:
                print("Please enter a positive amount.")
                continue
            return amount
        except ValueError:
            print("Invalid input. Please enter a numeric value.")