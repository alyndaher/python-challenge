import os
import csv

csvpath = os.path.join("election_data.csv")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    voterID = []
    county = []
    candidate = []

    for row in csvreader:
        voterID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

    #remove first position of headers from list 
    voterID.pop(0)
    county.pop(0)
    candidate.pop(0)


    #Title of Information
    print ("Election Results")
    print("-------------------------")

    #The total number of votes cast
    print ("Total Votes: " + str(len(voterID)))

    #formatting
    print("-------------------------")
    
    #A complete list of candidates who received votes
    unique_list = []

    for x in candidate:
        if x not in unique_list:
            unique_list.append(x)
            
    #The total number of votes each candidate won
    Khan = 0
    Correy = 0
    Li = 0
    OTooley = 0
    x = 0
    for x in candidate:
        if x == unique_list[0]:
            Khan += 1
        if x == unique_list[1]:
            Correy += 1
        if x == unique_list[2]:
            Li += 1
        if x == unique_list[3]:
            OTooley += 1
    

    #The percentage of votes each candidate won
    def percent(x):
        Total = len(voterID)
        return x/Total

    KP = round(percent(Khan)*100,3)
    CP = round(percent(Correy)*100,3)
    LP = round(percent(Li)*100,3)
    OP = round(percent(OTooley)*100,3)

    #Display Candidate Stats
    print("Khan: " + str(KP) + f'% ({Khan})')
    print("Correy: " + str(CP) + f'% ({Correy})')
    print("Li: " + str(LP) + f'% ({Li})')
    print("OTooley: " + str(OP) + f'% ({OTooley})')

    print("-------------------------")

    #The winner of the election based on popular vote.
    final_list = dict([("Khan",KP),("Correy",CP),("Li",LP),("OTooley",OP)])

    print("Winner: " + max(final_list, key = final_list.get))

