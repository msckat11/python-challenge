# Import libraries
import os
import csv

#
file_path = os.path.join("Resources", "budget_data.csv")
total_months = 0
net_profit_loss = 0

raw_pl_list = []
pl_change_list = []

print("Financial Analysis")
print("---------------------------")

with open(file_path, "r") as bankfile:
    csv_reader = csv.reader(bankfile, delimiter=",")
    csv_header = next(bankfile)
    for row in csv_reader:
        #Find Total Months and store in variable
        total_months = total_months + 1

        #Find net profit/loss by adding each month's profit/loss to the last
        net_profit_loss = net_profit_loss + float(row[1])

        #Pull all profit/loss values from each month and put them in the raw_pl_list
        raw_pl_list.append(row[1])

    first_pl_list = raw_pl_list.pop()
    second_pl_list = raw_pl_list.pop(0)

    #Store the first list value in a variable
    first_pl_value = raw_pl_list[0]

    while x < len(raw_pl_list):
        print(raw_pl_list)
        x = x+1


    print("Total Months: " + str(total_months))
    print("Total Profit/Loss: $" + str(net_profit_loss))
    print(pl_change_list)

bankfile.close()