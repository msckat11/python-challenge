# Import libraries
import os
import csv

#
file_path = os.path.join("Resources", "budget_data.csv")
total_months = 0
net_profit_loss = 0

raw_pl_list = []
pl_change_list = []


def pl_change(amt1, amt2):
    monthly_pl = float(amt2) - float(amt1)
    pl_change_list.append(monthly_pl)

    
    print("Financial Analysis")
    print("---------------------------")

with open(file_path, "r") as bankfile:
    csv_reader = csv.reader(bankfile, delimiter=",")
    csv_header = next(bankfile)
    for row in csv_reader:
        total_months = total_months + 1
        net_profit_loss = net_profit_loss + float(row[1])
        raw_pl_list.append(row[1])
    print("Total Months: " + str(total_months))
    print("Total Profit/Loss: $" + str(net_profit_loss))
    



    

bankfile.close()