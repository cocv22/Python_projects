#Separate file made to get information of the user, keeping the code overall more clean.
from datetime import datetime

date_format = "%d-%m-%Y"
categories = {"I": "Income", "E": "Expense"}

def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)

    try:
        valid_date = datetime.strptime(date_str, date_format) 
        return valid_date.strftime(date_format) #cleans up date user typed in and gives it to us in the fomat that we need.
    except ValueError:
        print("Date is invalid. Enter date in dd-mm-yyyy pls")
        return get_date(prompt, allow_default)

def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("Amount must be positive")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_category():
    category = input("Enter the category (I for 'Incomce' or E for 'Expense'): ").upper()
    if category in categories:
        return categories[category]
    
    print("Invalid catefory. Enter I for 'Incomce' or E for 'Expense'.")
    return get_category()

def get_description():
    return input("Enter a description (optional) ")