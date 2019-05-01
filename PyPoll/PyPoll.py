# Import Dependcies
import os
import csv

# Set Variables 
TotalVotes = 0
Candidates = {}
CandidatesPercent = {}
WinnerVotes = 0
Winner = []


#Set variables for csv paths 
csvpath = os.path.join('Resources', 'election_data.csv')
outputpath = os.path.join('Resources', 'Output.txt')

with open(csvpath, newline = "") as election_data:

    # CSV reader specifies delimiter and variable that holds contents    
    csvreader = csv.reader(election_data, delimiter = ",")
    # Read the header row
    next(csvreader, None)

    # Loop through rows and perform calcs
    for row in csvreader:

        # Count TotalVotes
        TotalVotes = TotalVotes + 1

        #Calc Candidates
        if row[2] in Candidates.keys():
            Candidates[row[2]] += 1
        else:
            Candidates[row[2]] = 1

        # Find percent of votes by candidate
        for key, value in Candidates.items():
            CandidatesPercent[key] = round((value/TotalVotes) * 100, 1)

        # Find Winner
        for key in Candidates.keys():
            if Candidates[key] > WinnerVotes:
                Winner = key
                WinnerVotes = Candidates[key]




# CreateOutput
print("Election Results")
print("-------------------------------------")
print("Total Votes: " + str(TotalVotes))
print("-------------------------------------")
for key, value in Candidates.items():
   print(key + ": " + str(CandidatesPercent[key]) + "% (" + str(value) + ")")
print("-------------------------------------")
print("Winner: " + Winner)
print("-------------------------------------")


# Create Output File
with open(outputpath, 'w') as file:
    file.write("Election Results \n")
    file.write("------------------------------------- \n")
    file.write("Total Votes: " + str(TotalVotes) + "\n")
    file.write("------------------------------------- \n")
    for key, value in Candidates.items():
        file.write(key + ": " + str(CandidatesPercent[key]) + "% (" + str(value) + ") \n")
    file.write("------------------------------------- \n")
    file.write("Winner: " + Winner + "\n")
    file.write("------------------------------------- \n")