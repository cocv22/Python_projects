import pandas as pd
import csv
from datetime import datetime

class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]
    
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
            
CSV.initialize_csv()
CSV.add_entry("20-07-2024", 125.65, "Income", "Salary")
