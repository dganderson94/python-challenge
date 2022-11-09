# import modules
import os
import csv
import statistics

# set file paths
csvpath = os.path.join('Resources', 'budget_data.csv')
txtpath = os.path.join('analysis','analysis.txt')

# open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # skip header
    csvheader = next(csvreader)

    # initialize variables
    months = 0
    total = 0
    change = []
    prevProfit = 0
    greatestInc = 0
    greatestDec = 0

    # read rows
    for row in csvreader:

        # count months
        months += 1

        # sum profits/losses
        total += int(row[1])

        # calculate changes
        latestChange = int(row[1]) - prevProfit
        change.append(latestChange)
        prevProfit = int(row[1])

        # greatest increase
        if latestChange > greatestInc:
            greatestInc = latestChange
            incMonth = row[0]

        # greatest decrease
        if latestChange < greatestDec:
            greatestDec = latestChange
            decMonth = row[0]

    # remove first member of change
    del change[0]

    # print it all out
    analysis = (
        "Financial Analysis\n"
        "----------------------------\n"
        f"Total Months: {months}\n"
        f"Total: ${total}\n"
        f"Average Change: ${round(statistics.mean(change),2)}\n"
        f"Greatest Increase in Profits: {incMonth} (${greatestInc})\n"
        f"Greatest Decrease in Profits: {decMonth} (${greatestDec})"
        )
    print(f"\n{analysis}\n")

# export text file
with open(txtpath, "w") as txtfile:
    txtfile.write(analysis)