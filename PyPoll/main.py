# Import libraries
import os
import csv
from collections import defaultdict

#Tell it where to get the csv file
file_path = os.path.join("Resources", "election_data.csv")

# #Create variables to count votes
# total_votes = 0

#Create empty lists and dictionaries to fill later
init_candidates = []
candidate_dict = defaultdict(int)

# #Open the csv file and read it
with open(file_path, "r") as vote_file:
    csv_reader = csv.reader(vote_file, delimiter=",")
    csv_header = next(vote_file)
    for row in csv_reader:
        init_candidates.append(row[2])
# print(init_candidates)

for name in init_candidates:
        candidate_dict[name] += 1
# print(candidate_dict)

Khan_votes = candidate_dict["Khan"]
# print(Khan_votes)
Correy_votes = candidate_dict["Correy"]
# print(Correy_votes)
Li_votes = candidate_dict["Li"]
# print(Li_votes)
Tooley_votes = candidate_dict["O'Tooley"]
# print(Tooley_votes)
        
all_votes = Khan_votes + Correy_votes + Li_votes + Tooley_votes
# print(all_votes)

Khan_percent = round((Khan_votes / all_votes * 100), 3)
# print(Khan_percent)
Correy_percent = round((Correy_votes / all_votes * 100), 3)
Li_percent = round((Li_votes / all_votes * 100), 3)
Tooley_percent = round((Tooley_votes / all_votes * 100), 3)

if Khan_votes > Correy_votes:
        if Khan_votes > Li_votes:
                if Khan_votes > Tooley_votes:
                        winner = "Kahn"
elif Correy_votes > Li_votes:
        if Correy_votes > Tooley_votes:
                winner = "Correy"
elif Li_votes > Tooley_votes:
        winner = "Li"
else:
        winner = "O'Tooley"


print("Election Results")
print("---------------------------")
print("Total Votes: " + str(all_votes))
print("---------------------------")
print("Khan: " + str(Khan_percent) + "%" + " (" + str(Khan_votes) + ")")
print("Correy: " + str(Correy_percent) + "%" + " (" + str(Correy_votes) + ")")
print("Li: " + str(Li_percent) + "%" + " (" + str(Li_votes) + ")")
print("O'Tooley: " + str(Tooley_percent) + "%" + " (" + str(Tooley_votes) + ")")
print("---------------------------")
print("Winner: " + winner)

new_file_path = os.path.join("Analysis", "election_analysis.txt")
with open(new_file_path, "w+") as analysisfile:
    print("Election Results")
    print("---------------------------")
    print("Total Votes: " + str(all_votes))
    print("---------------------------")
    print("Khan: " + str(Khan_percent) + "%" + " (" + str(Khan_votes) + ")")
    print("Correy: " + str(Correy_percent) + "%" + " (" + str(Correy_votes) + ")")
    print("Li: " + str(Li_percent) + "%" + " (" + str(Li_votes) + ")")
    print("O'Tooley: " + str(Tooley_percent) + "%" + " (" + str(Tooley_votes) + ")")
    print("---------------------------")
    print("Winner: " + winner)