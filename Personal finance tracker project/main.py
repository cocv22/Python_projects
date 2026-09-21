import pandas as pd
import csv
from datetime import datetime

class CSV:
    CSV_FILE = "finance_data.csv"
    
    @classmethod #Will have access to the class itself but not an instance of it.
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            # Gets a data frame explained in 4 columns, then we turn it into a CSV file with the same directory as the python file
            df = pd.DataFrame(columns=["date ", "amount ", "category ", "description "])
            df.to_csv(cls.CSV_FILE, index=False) #Index=False essentially means we're not gonna be sorting the dataframe by indexing it

CSV.initialize_csv()
