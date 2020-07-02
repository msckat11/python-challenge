# Import libraries
import os
import csv

#
file_path = os.path.join("Resources", "budget_data.csv")
total_months = 0
net_profit_loss = 0

raw_pl_list = []
pl_list1 = []
pl_list2 = []

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

    
    #Check creation of raw list
    print(raw_pl_list)
    
    print("---------------------------")
    
    #Creating the first zip list from the raw data list
    pl_list1 = raw_pl_list.copy()
    pl_list1.pop()

    print(pl_list1)
    
    #Creating the second zip list from the raw data list
    print("---------------------------")

    pl_list2 = raw_pl_list.copy()
    pl_list2.pop(0)
    
    print(pl_list2)
    
    print("---------------------------")

    pl_difference = []

    pl_zip = zip(pl_list1, pl_list2)
    for pl_list1, pl_list2 in pl_zip:
            pl_difference.append(float(pl_list2)-float(pl_list1))


    print("Total Months: " + str(total_months))
    print("Total Profit/Loss: $" + str(net_profit_loss))
    print(pl_difference)

bankfile.close()