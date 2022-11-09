# import modules
import os
import csv

# set file paths
csvpath = os.path.join('Resources', 'election_data.csv')
txtpath = os.path.join('analysis','analysis.txt')

# open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # skip header
    next(csvreader)

    # initialize variables
    total = 0
    candidateVotes = {}
    winningVotes = 0

    # read rows
    for row in csvreader:

        # count towards total votes
        total += 1

        # add vote to relevant candidate
        if row[2] in candidateVotes:
            candidateVotes[row[2]] += 1
        else:
            candidateVotes[row[2]] = 1 # adding new candidate if needed

    # write top bit
    header = (
        "Election Results\n"
        "-------------------------\n"
        f"Total Votes: {total}\n"
        "-------------------------\n"
    )

    # write middle bit
    body = ""
    for candidate in candidateVotes:
        body += (f"{candidate}: {str(round((candidateVotes[candidate] / total) * 100, 3))}% ({str(candidateVotes[candidate])})\n")
        
        # and also find out the winner while we're looking
        if candidateVotes[candidate] > winningVotes:
            winningVotes = candidateVotes[candidate]
            winner = candidate

    # write bottom bit
    footer = (
        "-------------------------\n"
        f"Winner: {winner}\n"
        "-------------------------"
    )

    # print it all out
    results = header + body + footer
    print(f"\n{results}\n")
    

# export text file
with open(txtpath, "w") as txtfile:
    txtfile.write(results)