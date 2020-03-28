
import os
import csv

csvpath = os.path.join('budget_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #add dictionary variable for csvfile data
    data = dict(csvreader)

#delete first position key, value pair (or header information)    
del data["Date"]

#split dictionary into two Lists called column1 and column2
column1 = [] 
column2 = [] 
items = data.items() 
for item in items: 
    column1.append(item[0]), column2.append(int(item[1]))

#The total number of months included in the dataset
total = len(column1)
print("Total Months: " + str(total))

#The net total amount of "Profit/Losses" over the entire period
Profit_Losses = sum(column2)
print("Total Profit/Loss: $"+ str(Profit_Losses))

#The average of the changes in "Profit/Losses" over the entire period

avgchange = [(n-column2[i-1]) if i else n for i,n in enumerate(column2)]
avgchange.pop(0)
avc = sum(avgchange)/len(avgchange)
print("Average Change: $" + str(round(avc,2)))

#The greatest increase in profits (date and amount) over the entire period
#combine column1 months with avgchange data into dictionary
avgchange.insert(0,0)
dict = {}
y=0

for i in column1:
    dict[i] = avgchange[y]
    y = y + 1

print("Greatest Increase in Profits: "+str(max(dict, key=dict.get)) + f' (${dict["Feb-2012"]})')

#The greatest decrease in losses (date and amount) over the entire 

print("Greatest Decrease in Profits: " +str(min(dict, key=dict.get)) + f' (${dict["Sep-2013"]})')