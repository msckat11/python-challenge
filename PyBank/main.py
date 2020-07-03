# Import libraries
import os
import csv

#
file_path = os.path.join("Resources", "budget_data.csv")
total_months = 0
net_profit_loss = 0

months = []
raw_pl_list = []
pl_list1 = []
pl_list2 = []
date_change_dict = {}

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

        #Pull each month's date and put them in the months list
        months.append(row[0])

    
    #Check creation of raw list
    # print(raw_pl_list)

    #Check creation of months list
    # print(months)
    
    #Creating the first zip list from the raw data list
    pl_list1 = raw_pl_list.copy()
    pl_list1.pop()

    #Check creation of pl_list1
    # print(pl_list1)
    
    #Creating the second zip list from the raw data list

    pl_list2 = raw_pl_list.copy()
    pl_list2.pop(0)
    
    #Check creation of pl_list2
    # print(pl_list2)

    #Create empty list to hold profit/loss changes as they are calculated
    pl_difference = []

    pl_zip = zip(pl_list1, pl_list2)
    for pl_list1, pl_list2 in pl_zip:
            pl_difference.append(float(pl_list2)-float(pl_list1))
    
    #Check creation of list holding profit/loss changes
    # print(pl_difference)

    #Calculate the average profit/loss change
    pl_avg_change = round(sum(pl_difference) / len(pl_difference), 2)
    # print(pl_avg_change)

    #Find the max value in pl_difference list
    pl_change_max = max(pl_difference)

    #Find the min value in pl_difference list
    pl_change_min = min(pl_difference)

    #Copy months list and remove first month
    dates = months.copy()
    dates.pop(0)

    # Check new dates list
    # print(dates)

    #Create dictionary with dates corresponding to profit/loss changes
    for i in range(len(dates)):
        date_change_dict[dates[i]] = pl_difference[i]

    #Check dictionary creation
    print(date_change_dict) 

    print("Total Months: " + str(total_months))
    print("Total Profit/Loss: $" + str(round(net_profit_loss)))
    print("Average Change: $ " + str(pl_avg_change))
    print("Greatest Increase in Profits: date here ($" + str(round(pl_change_max)) + ")")
    print("Greatest Decrease in Profits: date here ($" + str(round(pl_change_min)) + ")")
    

bankfile.close()