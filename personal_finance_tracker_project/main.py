import pandas as pd
import csv
from datetime import datetime
from data_entry import get_amount, get_category, get_description, get_date
import matplotlib.pyplot as plt

class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]
    FORMAT = "%d-%m-%Y"
    
    @classmethod #Will have access to the class itself but not an instance of it.
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            # Gets a data frame explained in 4 columns, then we turn it into a CSV file with the same directory as the python file
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False) #Index=False essentially means we're not gonna be sorting the dataframe by indexing it
    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }
        with open(cls.CSV_FILE, "a", newline ="") as csvfile: #stores opened files as the variable csvfile, so that it autimatically takes care of cleaning up essentially.
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added succesfully")
    
    @classmethod
    def get_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        #with panda you can access the column. Also, this converts all dates in the column to the specified format
        df["date"] = pd.to_datetime(df["date"], format=CSV.FORMAT)
        #Here we get the star_date string input and turn it into the correct format
        start_date = datetime.strptime(start_date, CSV.FORMAT)
        end_date = datetime.strptime(end_date, CSV.FORMAT)
        # & is used when working with pandas specifically.
        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        # Returns a df where the mask above is true
        filtered_df = df.loc[mask]
        
        if filtered_df.empty:
            print("No transactions found in the date range.")
        else:
            print(f"Transactions from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}")
            print(filtered_df.to_string(index=False, formatters={"date": lambda x: x.strftime(CSV.FORMAT)}))
        # This gets all the rows where category is equal to income, feature of panda      
            total_income = filtered_df[filtered_df["category"] == "Income"]["amount"].sum()
            total_expense = filtered_df[filtered_df["category"] == "Expense"]["amount"].sum()
            print("\nSummary:")
            print(f"Total Income: ${total_income:.2f}")
            print(f"Total Expense: ${total_expense:.2f}")
            print(f"Net savings: ${(total_income - total_expense):.2f}")
    
        return filtered_df
            
def add():
    CSV.initialize_csv()
    date = get_date("Enter the date of the transaction (dd-mm-yyyy) or press enter for today's date: ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)

def plot_transactions(df):
    #Index is the way in which we locate and manipulate different rows
    #We're using 'date' to find information by the date to create the plot
    df.set_index("date", inplace=True)
    #(fill)resample('D') makes a value for every single day, allowing for aggragation of different values on the same day
    #We sum values to get values on the same date and adding them.
    #reindex makes sure the spaces conform to the index that's been set, and fills empty values with zero
    income_df = (
        df[df["category"] == "Income"]["amount"]
        .resample("D")
        .sum()
        .reindex(df.index, fill_value=0)
        ) 
    expense_df = (
        df[df["category"] == "Expense"]["amount"]
        .resample("D")
        .sum()
        .reindex(df.index, fill_value=0)
        )
    #sets up scree for plot
    plt.figure(figsize =(15, 8))
    plt.plot(income_df.index, income_df, label="Income", color="g")
    plt.plot(expense_df.index, expense_df, label="Expense", color="r")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income and Expenses")
    #Allows the label for different colored lines to be visible.
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    while True:
        print("\n1. Add new transaction")
        print("2. View transactions and summary within a date range")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            add()
        elif choice == "2":
            start_date = get_date("Enter start date (dd-mm-yyyy): ")
            end_date = get_date("Enter end date (dd-mm-yyyy): ")
            df = CSV.get_transactions(start_date, end_date)
            if input("Would you like to see a plot? (y/n) ").lower() == "y":
                plot_transactions(df)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Enter a number 1-3.")

# Only runs if file is run directly. Essentially protects the main()/code in the main function
if __name__ == "__main__":
    main()
