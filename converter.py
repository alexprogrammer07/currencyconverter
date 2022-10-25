from forex_python.converter import CurrencyRates, CurrencyCodes     # Importing the required modules

currencyRates = CurrencyRates()  # Defining a class object to store currency rates
currencyCodes = CurrencyCodes()  # Creating a class object to store name and symbol of currency

"Try except block to handle exceptions"
try:
    choice = input("Enter 'r' for checking the rate\n"
        "Enter 'c' for converting currency\n"
        "Enter 's' to get symbol of a currency\n"
        "Enter 'n' to get name of the currency\n"
        "Your Choice: ").lower()  # Storing the choice of the user

    if choice == 'r' or choice == 'rate':
        code1 = input("Enter the Currency code (1): ").upper()
        code2 = input("Enter the Currency code (2): ").upper()

        print(currencyRates.get_rate(code1, code2))  # Printing the rate of currency

    elif choice == 'c' or choice == 'convert':
        code1 = input("Enter the Currency code (1)\t[From which you want to convert]: ").upper()
        code2 = input("Enter the Currency code (2)\t[To which you want to convert]: ").upper()

        amount = float(input("Enter the amount to be converted: "))  # Storing amount to be converted

        print(currencyRates.convert(code1, code2, amount))  # Printing the converted amount

    elif choice == 's' or choice == 'symbol':       #comparing the symbols
        code1 = input("Enter the Currency code of which you want symbol: ").upper()

        print(currencyCodes.get_symbol(code1)) # Printing the symbol of currency

    elif choice == 'n' or choice == 'name':
        code1 = input("Enter the Currency code of which you want name: ").upper()

        print(currencyCodes.get_currency_name(code1))  # Printing the name of the currency
    else:
        print("Please enter a valid choice !! :)")  # Printing message for invalid choice

except Exception as e:
    print(e)  # Printing the exception (if any)
