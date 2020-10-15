from forex_python.converter import CurrencyRates, CurrencyCodes

c = CurrencyRates()  # Defining a class object to store currency rates
code = CurrencyCodes()  # Creating a class object to store name and symbol of currency

try:
    choice = input("Enter 'r' for checking the rate\n"
                   "Enter 'c' for converting currency\n"
                   "Enter 's' to get symbol of a currency\n"
                   "Enter 'n' to get name of the currency\n").lower()  # Storing the choice of the user

    if choice == 'r' or choice == 'rate':
        code1 = input("Enter the Currency code (1):\n").upper()
        code2 = input("Enter the Currency code (2):\n").upper()

        print(c.get_rate(code1, code2))  # Printing the rate of currency

    elif choice == 'c' or choice == 'convert':
        code1 = input("Enter the Currency code (1)\t[From which you want to convert]:\n").upper()
        code2 = input("Enter the Currency code (2)\t[To which you want to convert]:\n").upper()

        amount = float(input("Enter the amount to be converted - \n"))  # Storing amount to be converted

        print(c.convert('USD', 'INR', amount))  # Printing the converted amount

    elif choice == 's' or choice == 'symbol':
        code1 = input("Enter the Currency code of which you want symbol:\n").upper()

        print(code.get_symbol(code1))

    elif choice == 'n' or choice == 'name':
        code1 = input("Enter the Currency code of which you want name:\n").upper()

        print(code.get_currency_name(code1))  # Printing the name of the currency
    else:
        print("Please enter a valid choice !! :)")  # Printing message for invalid choice

except Exception as e:
    print(e)
