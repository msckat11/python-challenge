# Import libraries
import os
import csv
from collections import defaultdict

#Tell it where to get the csv file
file_path = os.path.join("Resources", "election_data.csv")

#Create variables to count votes
total_votes = 0

#Create empty lists and dictionaries to fill later
init_candidates = []
Khan_votes = []
Correy_votes = []
Li_votes = []
Tooley_votes = []
Other_votes = []

vote_count = defaultdict(int)

#Print out heading
print("Election Results")
print("---------------------------")

# #Open the csv file and read it
with open(file_path, "r") as vote_file:
    csv_reader = csv.reader(vote_file, delimiter=",")
    csv_header = next(vote_file)
    for row in csv_reader:
        init_candidates.append(row[2])
print(init_candidates)

for name in init_candidates:
        vote_count[name] += 1
print(vote_count)

Khan_votes = vote_count["Khan"]
print(Khan_votes)
Correy_votes = vote_count["Correy"]
print(Correy_votes)
Li_votes = vote_count["Li"]
print(Li_votes)
Tooley_votes = vote_count["O'Tooley"]
print(Tooley_votes)
        
all_votes = Khan_votes + Correy_votes + Li_votes + Tooley_votes
print(all_votes)


        #Find Total Votes and store in variable
        # total_votes = total_votes + 1
        
        # #Find net profit/loss by adding each month's profit/loss to the last
        # net_profit_loss = net_profit_loss + float(row[1])

        # #Pull all candidate names from the csv file and put them in the init_candidates list
        # init_candidates.append(row[2])

        # #Count each candidate in init_candidates


                # Khan_total = Khan_votes.count()
                # print(Khan_total)
        

        
        # for name in init_candidates:
        #    vote_count[name] += 1

     
     

    
        # Check creation of init_candidates list - LOL, OMG NOT A GOOD IDEA FOR LARGE DATA SETS
        # print(init_candidates) - DONT DO IT

#     #Check creation of months list
#     # print(months)
    
#     #Creating the first zip list from the raw data list
#     pl_list1 = raw_pl_list.copy()
#     pl_list1.pop()

#     #Check creation of pl_list1
#     # print(pl_list1)
    
#     #Creating the second zip list from the raw data list
#     pl_list2 = raw_pl_list.copy()
#     pl_list2.pop(0)
    
#     #Check creation of pl_list2
#     # print(pl_list2)

#     #Create empty list to hold profit/loss changes as they are calculated
#     pl_difference = []

#     pl_zip = zip(pl_list1, pl_list2)
#     for pl_list1, pl_list2 in pl_zip:
#             pl_difference.append(float(pl_list2)-float(pl_list1))
    
#     #Check creation of list holding profit/loss changes
#     # print(pl_difference)

#     #Calculate the average profit/loss change
#     pl_avg_change = round(sum(pl_difference) / len(pl_difference), 2)
#     # print(pl_avg_change)

#     #Find the max value in pl_difference list
#     pl_change_max = max(pl_difference)

#     #Find the min value in pl_difference list
#     pl_change_min = min(pl_difference)

#     #Copy months list and remove first month
#     dates = months.copy()
#     dates.pop(0)

#     # Check new dates list
#     # print(dates)

#     #Create dictionary with dates corresponding to profit/loss changes
#     for i in range(len(pl_difference)):
#         date_change_dict[pl_difference[i]] = dates[i]

#     #Check dictionary creation
#     # print(date_change_dict) 

#     #Call the key pair for pl_change_max
#     pl_change_max_date = date_change_dict[pl_change_max]

#     #Check the new variable for the date matching the max
#     # print(pl_change_max_date)

#     #Call the key pair for pl_change_min
#     pl_change_min_date = date_change_dict[pl_change_min]

#     #Check the new variable for the date matching the min
#     # print(pl_change_min_date)

# print("Total Votes: " + str(total_votes))



# print("Total Profit/Loss: $" + str(round(net_profit_loss)))
# print("Average Change: $ " + str(pl_avg_change))
# print("Greatest Increase in Profits: " + str(pl_change_max_date) + " ($" + str(round(pl_change_max)) + ")")
# print("Greatest Decrease in Profits: " + str(pl_change_min_date) + " ($" + str(round(pl_change_min)) + ")")

# new_file_path = os.path.join("Analysis", "Financial_Analysis.txt")
# with open(new_file_path, "w+") as analysisfile:
#     print("Financial Analysis", file=analysisfile)
#     print("---------------------------", file=analysisfile)
#     print("Total Months: " + str(total_months), file=analysisfile)
#     print("Total Profit/Loss: $" + str(round(net_profit_loss)), file=analysisfile)
#     print("Average Change: $ " + str(pl_avg_change), file=analysisfile)
#     print("Greatest Increase in Profits: " + str(pl_change_max_date) + " ($" + str(round(pl_change_max)) + ")", file=analysisfile)
#     print("Greatest Decrease in Profits: " + str(pl_change_min_date) + " ($" + str(round(pl_change_min)) + ")", file=analysisfile)