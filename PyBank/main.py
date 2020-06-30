import os
import csv

file_path = os.path.join("Resources", "budget_data.csv")
total_months = 0
net_profit_loss = 0


with open(file_path) as csvfile:
    csv_reader = csv.reader(csvfile, delimeter=",")
    csv_header = next(csvfile)
    print(f"Header: {csv_header})

    # for row in csv_reader
