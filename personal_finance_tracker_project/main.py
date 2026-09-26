import pandas as pd
import csv
from datetime import datetime
from data_entry import get_amount, get_category, get_description, get_date

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
        df = pd.read.csv(cls.CSV_FILE)
        #with panda you can access the column. Also, this converts all dates in the column to the specified format
        df["date"] = pd.to_datetime(df["date"], format=CSV.FORMAT)
        #Here we get the star_date string input and turn it into the correct format
        start_date = datetime.strptime(start_date, CSV.FORMAT)

def add():
    CSV.initialize_csv()
    date = get_date("Enter the date of the transaction (dd-mm-yyyy) or press enter for today's date: ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)
            
add()
