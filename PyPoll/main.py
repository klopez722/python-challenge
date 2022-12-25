print ("Election Results")


print ("--------------------------------------------")

#import modules
import os
import csv

csvpath = os.path.join(".", "Resources", "election_data.csv")

with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    
    TotalVote = 0
    candidate = {}

    for row in csvreader:
        TotalVote += 1
        name = row[2]
        if name in candidate :
            candidate[name] += 1
        else: 
            candidate[name] = 1
        

    print("Total votes:" + str(TotalVote))

    print ("--------------------------------------------")
    
    #Calculate Charles votes
    candidate["Charles"] = round((candidate['Charles Casper Stockham']/TotalVote) * 100, 3)
    print("Charles Casper Stockham: " + str(candidate["Charles"]) + "% " + str(candidate["Charles Casper Stockham"]))
    
    #Calculate Diana votes
    candidate["Diana"] = round((candidate['Diana DeGette']/TotalVote) * 100, 3)
    print("Diana DeGette: " + str(candidate["Diana"]) + "% " + str(candidate["Diana DeGette"]))

    #Calculate Raymon votes
    candidate["Raymon"] = round((candidate['Raymon Anthony Doane']/TotalVote) * 100, 3)
    print("Raymon Anthony Doane: " + str(candidate["Raymon"]) + "% " + str(candidate["Raymon Anthony Doane"]))

    print ("--------------------------------------------")

    #Calculate winner
    candidate_winner = max(candidate, key=candidate.get)
    print("Winner: " + str(candidate_winner))

    print ("--------------------------------------------")

    #transfer results to txt file
    txt= open("Results.txt", "w")
    txt.write("Election Results" + "\n")
    txt.write("--------------------------------------------" + "\n")
    txt.write("Total Vote: " + str(TotalVote) + "\n")
    txt.write("--------------------------------------------" + "\n")
    txt.write("Charles Casper Stockham: " + str(candidate["Charles"]) + "% " + str(candidate["Charles Casper Stockham"]) + "\n")
    txt.write("Diana DeGette: " + str(candidate["Diana"]) + "% " + str(candidate["Diana DeGette"]) + "\n")
    txt.write("Raymon Anthony Doane: " + str(candidate["Raymon"]) + "% " + str(candidate["Raymon Anthony Doane"]) + "\n")
    txt.write("--------------------------------------------" + "\n")
    txt.write("Winner: " + str(candidate_winner) + "\n")
    txt.write("--------------------------------------------" + "\n")